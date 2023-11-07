import numpy as np
import pandas as pd
import re
import osmnx as ox
from config import osm_places
import matplotlib.colors as mcolors

class Normalized():
    def __init__(self, minn, maxn):
        self.minn = np.array(minn)
        self.maxn = np.array(maxn)
    
    def transform(self, data):
        return (data - self.minn) / (self.maxn - self.minn)

    def inverse_transform(self, data):
        return data * (self.maxn - self.minn) + self.minn

class StandardScaler():
    def __init__(self, mean, std):
        #self.mean = torch.tensor(mean)
        #self.std = torch.tensor(std)
        self.mean = np.array(mean)
        self.std = np.array(std)
    
    def transform(self, data):
        return (data - self.mean) / self.std

    def inverse_transform(self, data):
        return data * self.std + self.mean

def output_all_places():
    for i in osm_places:
        print(i)
    pass

def check(str):
    if str == 'place_name':
        output_all_places()
    elif str == 'osmnx_version':
        print(ox.__version__)
    pass

# 统一高程
def convert_height(height):
    try:
        if pd.isna(height):  # 逐个元素地应用pd.isna()函数
            return 0.
        if isinstance(height, str):
            if "foot" in height or "feet" in height:
                # 提取数字并转换为米
                number = float(re.findall(r'\d+\.?\d*', height)[0])
                return number * 0.3048
        try:
            return float(height)
        except Exception as d:
            return 0.
    except Exception as e:
        return 0.

def convert_geometry(geometry):
    pass
    
# 调整颜色
def adjust_color(color, amount):
    rgb = mcolors.hex2color(color)
    # 将RGB颜色转换为HSV颜色
    hsv = mcolors.rgb_to_hsv(np.array(rgb).reshape(1, -1))
    if np.isscalar(hsv):
        hsv -= amount * 0.3
    else:
        hsv[0][2] -= amount * 0.3
    # 将HSV颜色转换回RGB颜色
    rgb = mcolors.hsv_to_rgb(hsv)
    return mcolors.rgb2hex(rgb[0])

