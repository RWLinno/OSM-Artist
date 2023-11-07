import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import argparse

import folium
import osmnx as ox
import map_coloring as mc
import config
from utils import *

def main(args):
    check(args.check)
    map = mc.map(args)
    map.draw_height()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', type=str, default='')
    parser.add_argument('--place_name', type=str, default=config.default_place_name)
    parser.add_argument('--type',type=str,default='')
    parser.add_argument('--tags',type=dict,default=config.tags)
    parser.add_argument('--network_type',type=str,default='all')
    args = parser.parse_args()
    
    main(args)