import time
import argparse

import map_coloring as mc
import config
from utils import *

def main(args):
    start_time = time.time()
    #########################################
    check(args.check)
    map = mc.map(args)
    height_map = map.draw_height()
    basic_map = map.draw_basic()
    #map.print_all_info()    
    processed_map = map.blend_figures(basic_map,height_map)
    if args.save == 'yes':
        map.save_fig(height_map,'height')
        map.save_fig(basic_map,'basic')
        map.save_fig(processed_map,'processed')

    ########################################
    end_time = time.time()
    print("total run time:{} s".format(end_time - start_time))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', type=str, default='')
    parser.add_argument('--place_name', type=str, default=config.default_place_name)
    parser.add_argument('--type',type=str,default='')
    parser.add_argument('--tags',type=dict,default=config.tags)
    parser.add_argument('--figsize', type=tuple, default=config.default_figsize)
    parser.add_argument('--edge_linewidth', type=float, default=config.default_edge_linewidth)
    parser.add_argument('--save', type=str, default=config.default_save)
    parser.add_argument('--network_type',type=str,default='all')
    args = parser.parse_args()
    
    main(args)   