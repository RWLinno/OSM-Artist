# OSM-Artist
 A quick drawing tool based on the osmnx package and OpenStreetMap dataset.

Github : https://github.com/RWLinno/OSM-Artist

![processed](https://s2.loli.net/2023/11/07/Gz8wCDJEgQOVdmP.jpg)

###### Fig1. Overview of the processed map, placed at Montmartre, Paris, France



### Install

- Please create an environment that uses python version >= 3.8.3

```
conda create -n osmnx-artist python==3.11.6
conda activate osmnx-artist
```

- This library is mainly based on osmnx for mapping, other libraries are more commonly used. The following command gets the core libraries we need.

```
pip install osmnx
```

- Or you can use the requirements.txt exported from my experimental environment.

```
pip install -r requirements.txt
```



### Quick run

All you need to do is run our main.py file from the command line to quickly get the code working without any parameters!

```
python main.py [-check] [-place_name] [-type] [-tags] [-figsize] [-edge_linewidth] [-save] [-network_type] 
```

Parameter introduction:

- check -> str : check information about a field in the data
- place_name -> str:  find and obtain data for this place name in the OSM dataset online
- type -> str : what kind of map do you want to draw?
- tags -> dict : what map information comes with the displayed image
- figsize -> tuple : resulting image size
- edge_linewidth -> float : drawing stroke size
- save -> str : Save image results to `./output/place_name/type`
- network_type -> str : osmnx comes with a drawing style parameter, which by default draws out all traffic networks, etc.

However, most of the parameters can be tweaked by opening `config.py`, which I think is much more convenient.



### Draw Height_map

By **regularizing the height field** of the building at the site to the range [0-1], it is possible to represent the height of the building in a black-and-white plot, with darker colors being lofty and vice versa being low.

![height](https://s2.loli.net/2023/11/07/Dk1o86AdvSeWsVq.jpg)

###### Fig2. Height map of SoHo, New York, NY, a lot of uneven residential buildings there.



### Draw color_map

Color maps are drawn by making a **color mapping table** for each map element, e.g. we use blue for water and green for trees.

![basic](https://s2.loli.net/2023/11/07/RY9Ktr8MSZsfkUO.jpg)

###### Fig2. Basic colored map of Yellowstone National Park, United States, where there are a lot of woods and grass.



### Blend both

We use **image overlays** to combine heights with geographic elements to be able to represent a map well, and I think that's kind of a good combination.

![image-20231107142434274](https://s2.loli.net/2023/11/07/z2CSLQpTxvdkG7u.png)

###### Fig3. blend map is designed to create a greater variety of colors to differentiate between sites of the same type but different heights.



### Some Problems

- Many of the data formats in OSM are not harmonized, which leads to much more processing to be added to the project. Let's say the elements of height field are often missing, or has only a few values, or additional units like meters, feet, etc. that also need to be converted. Even some places such as Tianhe, Guangzhou will appear "A 区" in the height field :( 
- Because OSM is a kind of graph data, and because there are no marker points such as 'building' or 'natural' at all, you need to double-check before drawing a graph using the field
- There is a wide variety of elements and not all of them correspond to colors, so I use ash gray to represent unregistered elements (at least not in the places I look for by default), so the project needs to keep testing more places to represent a wide variety of OSM data in order to improve the visualization.



### To update

- Write a method to input data offline
- Process more unrecognized regions
- Optimize the map coloring algorithm

