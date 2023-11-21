osm_places = {
    "SoHo, New York, NY", #-74.0087049 40.7138231 -73.9900354 40.733357
    "Piedmont, California, USA",
    "Emeryville, California, USA",
    "Tianhe, GuangZhou, China",
    "Shibuya, Tokyo, Japan", #time out
    "The Colosseum, Rome, Italy",
    "The Kremlin, Moscow, Russia", #time out
    "Times Square, New York City, United States",
    "Harajuku, Tokyo, Japan", #  Found no graph nodes within the requested polygo
    "Montmartre, Paris, France",
    "Red Square, Moscow, Russia",
    "Piazza Navona, Rome, Italy",
    "Bondi Beach, Sydney, Australia",
    "Luxor Temple, Luxor, Egypt", #time out
    "Golden Gate Bridge, San Francisco, United States", #time out
    "Yellowstone National Park, United States"
}

default_type = "place_name"
default_place_name = "SoHo, New York, NY"
data_path = "./data/"
from_file = ""#"maldives-latest.osm.bz2"
default_edge_linewidth = 0.1
default_figsize=50
default_bbox = (-74.0087049,40.7138231,-73.9900354,40.733357) #None # west, south, east, north
default_save = 'yes'

tags = {
    'highway': True,
    'traffic_signals': True,
    'crossing': True,
    'kerb': True,
    'button_operated': True,
    'tactile_paving': True,
    'building': True, 
    'ele': True,
    'railway': True,
    'barrier': True,
    'tourism': True,
    'natural': True,
    'cycleway': True,
    'amenity': True,
    'parking': True,
    'service': True,
    'sidewalk': True,
    'landuse': True,
    'footway': True,
    'water': True,
    'street':True,
    'ways':True
}

color_mapping = {
    'highway': '#FF0000',  # 红色
    'traffic_signals': '#FFA500',  # 橙色
    'crossing': '#FFFF00',  # 黄色
    'kerb': '#00FF00',  # 绿色
    'button_operated': '#00FFFF',  # 青色
    'tactile_paving': '#0000FF',  # 蓝色
    'building': '#800080',  # 紫色
    'ele': '#FF00FF',  # 粉色
    'railway': '#FFC0CB',  # 淡粉色
    'barrier': '#8B4513',  # 棕色
    'tourism': '#008000',  # 深绿色
    'natural': '#008080',  # 深青色
    'cycleway': '#808080',  # 灰色
    'amenity': '#FF1493',  # 深粉色
    'parking': '#FF4500',  # 深橙色
    'service': '#FFFF00',  # 黄色
    'sidewalk': '#D2B48C',  # 深卡其布色
    'landuse': '#FF69B4',  # 热情的粉红色
    'footway': '#00FF00',  # 绿色
    'water': '#0000FF',  # 蓝色
    'street': '#808080',  # 灰色
    'ways': '#808080'  # 灰色
}