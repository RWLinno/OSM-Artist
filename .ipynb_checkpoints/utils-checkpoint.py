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
    if isinstance(height, str):
        if "foot" in height or "feet" in height:
            # 提取数字并转换为米
            number = float(re.findall(r'\d+\.?\d*', height)[0])
            return number * 0.3048
    if isinstance(height, (int, float)):
        # 假设其他数字默认为米
        return float(height)
    return float(0)

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

