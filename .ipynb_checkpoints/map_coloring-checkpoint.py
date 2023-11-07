import osmnx as ox
import utils
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import geopandas as gpd

class map():
    def __init__(self,args):
        super().__init__()
        self.place_name = args.place_name
        self.graph = ox.graph_from_place(self.place_name, network_type=args.network_type)
        self.gdf = ox.features_from_place(self.place_name, args.tags)
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
            print(f'{col}:{self.gdf[col].unique()}')
    
    def color_mapping():
        print("color_mapping")
        building_categories = self.gdf['building'].unique()
        color_mapping = {category: "#{:02x}{:02x}{:02x}".format(100,100,100) for category in building_categories}
        self.gdf['color']=self.gdf['building'].map(color_mapping)
        self.gdf.loc[self.gdf['natural'].isin(['spring', 'water']), 'color'] = 'blue'
        self.gdf.loc[self.gdf['natural'].isin(['sand', 'cliff']), 'color'] = 'yellow'
        self.gdf.loc[self.gdf['natural'].isin(['tree', 'grassland','wood','shrubbery']), 'color'] = 'green'
        self.gdf['color'] = self.gdf['color'].fillna('grey')
        self.gdf['norm_h'] = self.gdf['norm_h'].fillna(0.)
    
    def draw_basic(self):
        print("draw_basic")
        fig = ox.plot.plot_footprints(self.gdf, ax=None, figsize=(300, 300), color=self.gdf['color'], edge_color='black', edge_linewidth=1, alpha=None, bgcolor='white', bbox=None, save=True, show=True, close=False, filepath=None, dpi=600)
        return fig

    def check_data(self,x,name=None):
        print("check ",name)
        print("check_null:",x.isnull().sum())
    
    def draw_height(self):
        print("draw_height")
        # 绘制建筑物高度图
        fig, ax = ox.plot_footprints(self.gdf, edge_color="black", bgcolor="white", edge_linewidth=1, figsize=(8, 8), show=False)
        # 将高度转换为统一格式
        self.gdf["height"] = utils.convert_height(self.gdf["height"])
        
        self.check_data(self.gdf['height'],"height")
        self.check_data(self.gdf['geometry'],"geometry")
        
        # 创建一个新的GeoDataFrame，只包含多边形几何对象
        self.gdf_polygons = self.gdf[self.gdf["geometry"].apply(lambda geom: isinstance(geom, Polygon))]
        # 根据高度信息设置建筑物颜色（例如，高度越高，颜色越深）
        for polygon, height in zip(self.gdf["geometry"], self.gdf["height"]):
            if polygon is None or height is None:
                print("Find none!")
                print(polygon)
                print(height)
                continue
            if isinstance(polygon, Polygon):
                if len(polygon.exterior.coords) >= 3:
                    color = plt.cm.viridis(height / self.gdf["height"].max())  # 使用颜色映射函数设置颜色
                    ax.add_patch(plt.Polygon(list(polygon.exterior.coords), facecolor=color, edgecolor="black"))
        plt.title("Height map of buildings")
        plt.axis("off")
        plt.show()

    def save_fig(fig,name,color='white'):
        fig.savefig(f'output/{name}.png',facecolor=color)
