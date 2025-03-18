from prettymaps import *
from matplotlib import pyplot as plt

# 创建图床
fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

dilate = 100

layers = plot(
    'Alfama (945061630)', radius = 800, # 半径
    ax = ax, # 绑定图床
    layers = {
        'perimeter': {'circle': False, 'dilate': dilate}, # 控制绘图模式，{}即相当于圆形绘图模式
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
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
        'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
        'parking': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
        'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},

'coastline':{
    'file_location':'/home/bnb/Documents/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
    'buffer':100000,
    'circle':False
},

    },

    osm_credit = {'color': '#2F3737'}
)

print("savefig")

plt.savefig('map.png', dpi=200)
plt.savefig('map.svg')
