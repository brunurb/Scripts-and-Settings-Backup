from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union
from palettable.wesanderson import Zissou_5

def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers


fig, ax = plt.subplots(figsize = (15, 15), constrained_layout = True)

dilate = 100
doCircle = False

layers = plot(
    'Alcântara, Lisbon, Portugal',
    # Or coordinates  (38.6921,-9.3239)

    ax = ax,

    postprocessing = postprocessing,



    layers = {
            'perimeter': {},
            'streets': {
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
            'building': {'tags': {'building': True}, 'union': False,'circle': doCircle, 'dilate': dilate},
            'water': {'tags': {'natural': ['water', 'bay', 'wetland'], 'waterway': ['ditch', 'stream', 'weir'], 'landuse': ['basin', 'reservoir'], 'water': True},'circle': doCircle, 'dilate': dilate},
            'green': {'tags': {'landuse': ['grass', 'allotments', 'village_green', 'allotments', 'nature_reserve', 'recreation_ground', 'cemetery', 'meadow'], 'natural': ['island', 'grassland', 'scrub'], 'leisure': ['park', 'garden', 'sports_centre', 'playground']},'circle': doCircle, 'dilate': dilate},
            'cemeterystuff': {'tags': {'landuse': ['cemetery']},'circle': doCircle, 'dilate': dilate},
            'railway': {'custom_filter': '["railway"~"rail|light_rail|subway|tram|narrow_gauge"]', 'width': 2,'circle': doCircle, 'dilate': dilate},
            'forest': {'tags': {'landuse': ['forest'], 'natural': ['wood']},'circle': doCircle, 'dilate': dilate},
            'agriculture': {'tags':{'landuse': ['farmland']},'circle': doCircle, 'dilate': dilate},
            'developingLand': {'tags': {'landuse': ['brownfield', 'greenfield', 'construction', 'quarry', 'landfill']},'circle': doCircle, 'dilate': dilate},
            'sportstuff': {'tags': { 'leisure': ['pitch', 'track'] },'circle': doCircle, 'dilate': dilate},
            'parkplatz': {'tags': {'amenity': ['parking'], 'aeroway': ['apron', 'runway', 'taxiway']},'circle': doCircle, 'dilate': dilate},
            'gleisbett': {'tags': {'landuse': ['railway', 'industrial']},'circle': doCircle, 'dilate': dilate},
            'highway': {'tags': {'highway': ['footway', 'sideway', 'sidewalk', 'pedestrian', 'unclassified', 'construction']},'circle': doCircle, 'dilate': dilate},
            'place': {'tags': {'place': ['neighbourhood', 'quarter', 'suburb', 'residential', 'commercial', 'city_block']},'circle': doCircle, 'dilate': dilate},
            'man_made': {'tags': {'man_made': ['bridge', 'viaduct']},'circle': doCircle, 'dilate': dilate},


        },

        drawing_kwargs = {
            'background': {'fc': '#69a6bf', 'ec': '#dadbc1', 'zorder': -1},
            'perimeter': {'fc': '#64805b', 'ec': '#b2b6b7', 'lw': 6, 'zorder': 0},
            'green': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 1, 'zorder': 1},
            'water': {'fc': '#79a5ec', 'ec': '#94c6ee', 'lw': 0, 'zorder': 9},
            'streets': {'fc': '#f2d8bf', 'lw': 0, 'zorder': 4},
            'building': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0.1, 'zorder': 9},
            'railway': {'fc': '#a2c2db', 'ec': '#FF0000', 'alpha': 1, 'lw': 0, 'zorder': 8},
            'forest': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0, 'zorder': 1},
            'agriculture': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0, 'zorder': 1},
            'developingLand': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0, 'zorder': 8},
            'sportstuff': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0.3, 'zorder': 8},
            'parkplatz': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0.1, 'zorder': 3},
            'gleisbett': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0, 'zorder': 7},
            'cemeterystuff': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0, 'zorder': 9},
            'highway': {'fc': '#46693b', 'ec': '#ffffff', 'lw': 0, 'zorder': 11},
            'place': {'palette': ['#fcde9c', '#faa476', '#f0746e', '#dc3977', '#b9257a', '#e34f6f', '#7c1d6f'], 'lw': 0, 'zorder': 6},
            'man_made': {'fc': '#b52812', 'ec': '#ffffff', 'lw': 0, 'zorder': 10},

'coastline':{
    'file_location':'/home/bnb/Documents/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
    'buffer':100000,
    'circle':False
},

        },
        osm_credit = {'color': '#3b4545'}
)

print("savefig")

plt.savefig('map.png', dpi=200)

