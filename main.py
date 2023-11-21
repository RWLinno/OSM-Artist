import time
import argparse
import matplotlib.pyplot as plt
import map_coloring as mc
import config
from utils import *
import matplotlib.image as mpimg


def main(args):
    start_time = time.time()
    #########################################
    check(args.check)
    map = mc.map(args)
    height_map = map.draw_height()
    basic_map = map.draw_basic()
    #map.print_all_info()    
    processed_map = map.blend_figures(basic_map,height_map)
    plt.show()
    if args.save == 'yes':
        map.save_fig(height_map,'height')
        map.save_fig(basic_map,'basic')
        map.save_fig(processed_map,'processed')
        plt.show()
        # 显示结果
        '''
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        image1 = mpimg.imread('output/'+args.place_name+'/basic.jpg')
        image2 = mpimg.imread('output/'+args.place_name+'/height.jpg')
        image3 = mpimg.imread('output/'+args.place_name+'/processed.jpg')
        ax1.imshow(image1)
        ax1.set_title('basic')
        ax2.imshow(image2)
        ax2.set_title('height')
        ax3.imshow(image3)
        ax3.set_title('blended')
        # 显示整个图形
        plt.show()
        '''
    ########################################
    end_time = time.time()
    print("total run time:{} s".format(end_time - start_time))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', type=str, default='')
    parser.add_argument('--data_path', type=str, default=config.data_path)
    parser.add_argument('--from_file', type=str, default=config.from_file)
    parser.add_argument('--place_name', type=str, default=config.default_place_name)    
    parser.add_argument('--bbox', type=float, nargs='+', default=config.default_bbox)
    parser.add_argument('--type',type=str,default=config.default_type)
    parser.add_argument('--tags',type=dict,default=config.tags)
    parser.add_argument('--figsize', type=float, default=config.default_figsize)
    parser.add_argument('--edge_linewidth', type=float, default=config.default_edge_linewidth)
    parser.add_argument('--save', type=str, default=config.default_save)
    parser.add_argument('--network_type',type=str,default='all')
    args = parser.parse_args()
    print(args)
    main(args)