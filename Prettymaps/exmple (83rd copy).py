from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union
# 创建图床
fig, ax = plt.subplots(figsize = (12, 12),
constrained_layout = True)


dilate = 100
doCircle = False

layers = plot(

  (38.70789,-9.13449), # round core coordinate, format: (latitude, longitude)
  #Set radius for the map
  radius = 600,

    ax = ax, # 绑定图床
    layers = {
                     'perimeter': {'fill': True, 'lw': 0, 'zorder': 0}, # 控制绘图模式，{}即相当于圆形绘图模式
        # 下面的参数用于定义从OsmStreetMap选择获取的矢量图层要素，不了解的无需改动照搬即可
        'streets': {
            'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
            'width': {
                'motorway': 5,
                'trunk': 5,
                'primary': 4.5,
                'secondary': 4,
                'tertiary': 3.5,
                'residential': 3,
                'service': 2,
                'unclassified': 2,
                'pedestrian': 2,
                'footway': 1,
            },
            'circle': False, 'dilate': dilate
        },
        'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False, 'circle': False, 'dilate': dilate},
        'water': {'tags': {'natural': ['water', 'bay']}, 'circle': False, 'dilate': dilate},
        'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}, 'circle': False, 'dilate': dilate},
        'forest': {'tags': {'landuse': 'forest'}, 'circle': False, 'dilate': dilate},
        'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False, 'dilate': dilate}
    },
    # 下面的参数用于定义OpenStreetMap中不同矢量图层的样式，嫌麻烦的直接照抄下面的官方示例即可
    drawing_kwargs = {

            'perimeter': {'fc': '#B4D5A8', 'lw': 0, 'zorder': 0},
            'green': {'fc': '#B4D5A8', 'ec': '#B4D5A8', 'lw': 0, 'zorder': 1},
            'forest': {'fc': '#B4D5A8', 'ec': '#B4D5A8', 'lw': 0, 'zorder': 1},
            'water': {'fc': '#59ACB8', 'lw': 0, 'zorder': 3},
        'parking': {'fc': '#F6EBD1', 'lw': 0, 'zorder': 3},
            'streets': {'fc': '#C64C53', 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#FAD1D2', '#F8BBBD'], 'ec': '#C64C53', 'lw': 1, 'zorder': 4},


'coastline':{
    'file_location':'/home/bnb/Documents/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
    'buffer':100000,
    'circle':False
},

    },

    osm_credit = {'color': '#ffffff'}
)


ax.autoscale(enable=True, tight=True)


print("savefig")

plt.savefig('map.png', dpi=200)
plt.savefig('map.svg')
