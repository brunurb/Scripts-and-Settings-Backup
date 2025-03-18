from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union

def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers

fig, ax = plt.subplots(figsize = (20, 20), constrained_layout = True)

dilate = 100
doCircle = False

layers = plot(
    'Santa Maria Maior (6427496)',

    ax = ax,
    postprocessing = postprocessing,
    layers = {
        'perimeter': {'circle': False,},
            'streets': {
            'circle': False,
                'width': {
                    'motorway': 8,
                    'motorway_link': 3,
                    'service': 1,
                    'trunk': 6,
                    'primary': 6,
                    'secondary': 5,
                    'tertiary': 4,
                    'residential': 2,
                    'living_street': 2,
                    'pedestrian': 1.25,
                    'footway': 1.25,
                    'sideway': 1.25,
                    'track': 1,
                    'bridleway': 1,
                    'cycleway': 1,
                    'path': 0.5,
                    'unclassified': 3,
                    'construction': 1,
                }
            },
            'building': {'circle': False,'tags': {'building': True}, 'union': False},
            'water': {'circle': False,'tags': {'natural': ['water', 'bay', 'wetland'], 'waterway': ['ditch', 'stream', 'weir'], 'landuse': ['basin', 'reservoir'], 'water': True}},


'coastline':{'circle': False,
    'file_location':'/home/bnb/Documents/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
    'dilate':True,
    'buffer':100000,
},


'water': {
    'circle': False,
    'tags':{
        'waterway': True,
        'water': True,
        'harbour': True,
        'marina': True,
        'bay': True,
        'river': True,
        'dilate':True,
    },
}, 
            'green': {'circle': False,'tags': {'landuse': ['grass', 'allotments', 'village_green', 'allotments', 'nature_reserve', 'recreation_ground', 'cemetery', 'meadow'], 'natural': ['island', 'grassland', 'scrub'], 'leisure': ['park', 'garden', 'sports_centre', 'playground']}},
            'cemeterystuff': {'circle': False,'tags': {'landuse': ['cemetery']}},
            'railway': {'circle': False,'custom_filter': '["railway"~"rail|light_rail|subway|tram|narrow_gauge"]', 'width': 2},
            'forest': {'circle': False,'tags': {'landuse': ['forest'], 'natural': ['wood']}},
            'agriculture': {'circle': False,'tags':{'landuse': ['farmland']}},
            'developingLand': {'circle': False,'tags': {'landuse': ['brownfield', 'greenfield', 'construction', 'quarry', 'landfill']}},
            'sportstuff': {'circle': False,'tags': { 'leisure': ['pitch', 'track'] }},
            'parkplatz': {'circle': False,'tags': {'amenity': ['parking'], 'aeroway': ['apron', 'runway', 'taxiway']}},
            'gleisbett': {'circle': False,'tags': {'landuse': ['railway', 'industrial']}},
            'highway': {'circle': False,'tags': {'highway': ['unclassified', 'construction']}},
            'place': {'circle': False,'tags': {'place': ['neighbourhood', 'quarter', 'suburb', 'residential', 'commercial', 'city_block']}},
            'man_made': {'circle': False,'tags': {'man_made': ['bridge', 'viaduct']}},
            'garden': {'circle': False,'tags': {'leisure': 'garden'}},
            

        },

        drawing_kwargs = {
            'background': {'fc': '#69a6bf', 'ec': '#dadbc1', 'zorder': -1},
            'perimeter': {'fc': '#bebe8e', 'ec': '#999999', 'lw': 0, 'zorder': 0},
            'green': {'fc': '#5dab4d', 'ec': '#89fa73', 'lw': 0.5, 'zorder': 1},
            'water': {'fc': '#64a3e3', 'ec': '#2d4a80', 'lw': 0, 'zorder': 1},
            'streets': {'fc': '#F1E6D0', 'ec': '#2F3737', 'lw': 1, 'zorder': 2},
            'building': {'palette': ['#f58877', '#b35344', '#e37242', '#bd5022'], 'ec': '#2F3737', 'lw': 0.5, 'zorder': 15},
            'railway': {'fc': '#f5e673', 'ec': '#453a31', 'lw': 2, 'zorder': 12},
            'forest': {'fc': '#427a36', 'ec': '#7a8a57', 'lw': 0.5, 'zorder': 1},
            'agriculture': {'fc': '#345e2b', 'ec': '#647031', 'lw': 0.5, 'zorder': 1},
            'developingLand': {'fc': '#315c24', 'ec': '#2F3737', 'lw': 0.5, 'zorder': 8},
            'sportstuff': {'fc': '#42423a', 'ec': '#ffffff', 'lw': 0.5, 'zorder': 8},
            'parkplatz': {'fc': '#7a7649', 'ec': '#32512b', 'lw': 0.5, 'zorder': 3},
            'gleisbett': {'fc': '#7BAE82', 'ec': '#2d4a80', 'lw': 0.5, 'zorder': 7},
            'cemeterystuff': {'fc': '#2F3737', 'ec': '#2d4a80', 'lw': 0.5, 'zorder': 14},
            'highway': {'fc': '#46693b', 'ec': '#ffffff', 'lw': 0.5, 'zorder': 10},
            'place': {'fc': '#bea08e', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 6},
            'man_made': {'fc': '#b52812', 'ec': '#ffffff', 'lw': 2, 'zorder': 16},
            'garden': {'fc': '#a9d1a9', 'ec': '#8ab58a', 'lw': 1, 'zorder': 1},
            'coastline': {'fc': '#64a3e3', 'ec': '#2d4a80', 'lw': 1, 'zorder': 2}
        },
        osm_credit = {'color': '#3b4545'}
)



print("savefig")

plt.savefig('map.png', dpi=200)
plt.savefig('map.svg')
