import os
import osmnx as ox
import utils
import config
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from PIL import Image

class map():
    def __init__(self,args):
        super().__init__()
        self.place_name = args.place_name
        self.graph = ox.graph_from_place(self.place_name, network_type=args.network_type)
        self.gdf = ox.features_from_place(self.place_name, args.tags)
        self.figsize = args.figsize
        print("new map created")
        
    def print_graph(self):
        print("图的节点数:", len(self.graph.nodes))
        print("图的边数:", len(self.graph.edges))
        ox.plot_graph(ox.project_graph(self.graph)) 

    def print_all_info(self):
        print("graph columns:",self.gdf.columns)
        print(self.gdf.head())
        print(self.gdf.info())
        for col in self.gdf.columns:
            try:
                unique_values = self.gdf[col].apply(lambda x: tuple(x) if isinstance(x, list) else x).unique()
                print(f'{col}: {unique_values}')
            except Exception as e:
                print(f'Error occurred for column {col}: {str(e)}')
                continue
    
    def color_mapping(self):
        print("color_mapping")
        for column in self.gdf.columns:
            if column in config.color_mapping and not self.gdf[column].isnull().all():
                self.gdf.loc[~self.gdf[column].isnull(), 'color'] = config.color_mapping[column]
        try:
            self.gdf.loc[self.gdf['natural'].isin(['spring', 'water']), 'color'] = '#ADD8E6'  # 亮蓝色
            self.gdf.loc[self.gdf['natural'].isin(['sand', 'cliff']), 'color'] = '#FFFF00'  # 黄色
            self.gdf.loc[self.gdf['natural'].isin(['tree', 'grassland', 'wood', 'shrubbery']), 'color'] = '#00FF00'  # 绿色
        except Exception as e:
            print("No natrual")
        try:
            self.gdf.loc[self.gdf['building'] == 'residential', 'color'] = '#87CEFA'  # 淡蓝色
            self.gdf.loc[self.gdf['building'] == 'commercial', 'color'] = '#FF00FF'  # 紫色
            self.gdf.loc[self.gdf['building'] == 'industrial', 'color'] = '#FFA500'  # 橙色
        except Exception as e:
            print("No building")
        self.gdf['color'] = self.gdf['color'].fillna('grey') # 其余填充灰色
    
    def draw_basic(self):
        print("draw_basic")
        self.gdf['color'] = '#999999'
        try :
            self.gdf['color'] = self.gdf['building:colour'].fillna('#999999')
        except Exception as e:
            print("No building_color")
        self.color_mapping()
        print(self.gdf['color'].unique())
        #fig, ax = ox.plot.plot_footprints(self.gdf, color=self.gdf['color'], edge_color='black', bgcolor='white', edge_linewidth=0.5, alpha=None, bbox=None, save=True, show=True, close=False, filepath=None, dpi=600)
        fig, ax = ox.plot.plot_footprints(self.gdf, figsize = self.figsize, color=self.gdf['color'], edge_color='black', bgcolor='white', edge_linewidth=0.1)
    
        # plt.title("Basic map")
        plt.axis("off")
        return fig

    def check_data(self,x,name=None):
        print("check ",name)
        print("check_null:",x.isnull().sum())
    
    def draw_height(self):
        print("draw_height")
        # 绘制建筑物高度图
        fig, ax = ox.plot_footprints(self.gdf, figsize = self.figsize, color='white',edge_color="black", bgcolor="white", edge_linewidth=0.1, show=False)
        # 将高度转换为统一格式
        # print("before:",self.gdf["height"].unique())
        self.gdf["height"] = self.gdf["height"].apply(utils.convert_height)
        # 将高度归一化
        # print("after:",self.gdf["height"].unique())
        #print('mean:{%f},std:{%f}',self.gdf['height'].mean(),self.gdf['height'].std())
        
        scaler = utils.Normalized(self.gdf['height'].min(),self.gdf['height'].max()) 
        self.gdf['nh'] = 1. - scaler.transform(self.gdf['height']) # 统一到 [0,1] 范围
        #print("max:",self.gdf['nh'].max())
        
        #self.check_data(self.gdf['height'],"height")
        #self.check_data(self.gdf['nh'],"nh")
        #self.check_data(self.gdf['geometry'],"geometry")
        
        # 创建一个新的GeoDataFrame，只包含多边形几何对象
        self.gdf_polygons = self.gdf[self.gdf["geometry"].apply(lambda geom: isinstance(geom, Polygon))]
        # 根据高度信息设置建筑物颜色（例如，高度越高，颜色越深）
        for polygon, height in zip(self.gdf["geometry"], self.gdf["nh"]):
            # print(height,end="")     
            if polygon is None or height is None:
                print("Find none!")
                continue
            if isinstance(polygon, Polygon):
                try:
                #if len(polygon.exterior.coords) >= 3:
                    ax.add_patch(plt.Polygon(list(polygon.exterior.coords), facecolor=(height,height,height), edgecolor="black"))
                except Exception as e:
                    print("find polygon error!")
                    continue
        # plt.title("Height map")
        plt.axis("off")
        return fig

    def multiply_tuple(self, tup, num):
        return tuple (i * num for i in tup)

    def blend_figures(self, fig1, fig2):
        # 将 Figure 对象转换为 PIL 的 Image 对象
        fig1_image = fig1.canvas.tostring_rgb()
        fig1_width, fig1_height = fig1.canvas.get_width_height()
        image1 = Image.frombytes('RGB', (fig1_width, fig1_height), fig1_image)

        fig2_image = fig2.canvas.tostring_rgb()
        fig2_width, fig2_height = fig2.canvas.get_width_height()
        image2 = Image.frombytes('RGB', (fig2_width, fig2_height), fig2_image)

        # 确保两个图像具有相同的尺寸
        #image1 = image1.resize(image2.size)
        if image1.size != image2.size:
            print("no same shape!!!")
            return None
        
        # 获取图像的像素数据
        pixels1 = image1.load()
        pixels2 = image2.load()

        # 创建一个新的图像对象，用于存储融合后的图像
        blended_image = Image.new('RGB', image1.size)

        # 获取新图像的像素数据
        blended_pixels = blended_image.load()

        # 遍历每个像素，并计算颜色值的均值
        for i in range(image1.width):
            for j in range(image1.height):
                r1, g1, b1 = pixels1[i, j]
                r2, g2, b2 = pixels2[i, j]

                # 计算颜色值的均值
                blended_r = (r1 + r2) // 2
                blended_g = (g1 + g2) // 2
                blended_b = (b1 + b2) // 2

                # 将均值赋值给新图像的对应像素
                blended_pixels[i, j] = (blended_r, blended_g, blended_b)

        # 创建一个新的 Figure 对象，并将融合后的图像绘制上去
        plt.close()
        fig = plt.figure(figsize= self.figsize) # 没搞懂为什么缩水了
        plt.imshow(blended_image)
        plt.axis('off')
        plt.show()
        return fig

    def save_fig(self,fig,name,color='white',pre='',suf='.jpg'):
        if pre == '':
            pre = self.place_name
        
        # 创建目录
        output_dir = f'output/{pre}'
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存图像
        fig.savefig(f'{output_dir}/{name}{suf}', facecolor=color)