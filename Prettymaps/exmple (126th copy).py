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


fig, ax = plt.subplots(figsize = (15, 15), constrained_layout = True)
fig.patch.set_facecolor('#F9F8F8')


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
            'building': {'tags': {'building': True}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay', 'wetland'], 'waterway': ['ditch', 'stream', 'weir'], 'landuse': ['basin', 'reservoir'], 'water': True}},
            'green': {'tags': {'landuse': ['grass', 'allotments', 'village_green', 'allotments', 'nature_reserve', 'recreation_ground', 'cemetery', 'meadow'], 'natural': ['island', 'grassland', 'scrub'], 'leisure': ['park', 'garden', 'sports_centre', 'playground']}},
            'cemeterystuff': {'tags': {'landuse': ['cemetery']}},
            'railway': {'custom_filter': '["railway"~"rail|light_rail|subway|tram|narrow_gauge"]', 'width': 2},
            'forest': {'tags': {'landuse': ['forest'], 'natural': ['wood']}},
            'agriculture': {'tags':{'landuse': ['farmland']}},
            'developingLand': {'tags': {'landuse': ['brownfield', 'greenfield', 'construction', 'quarry', 'landfill']}},
            'sportstuff': {'tags': { 'leisure': ['pitch', 'track'] }},
            'parkplatz': {'tags': {'amenity': ['parking'], 'aeroway': ['apron', 'runway', 'taxiway']}},
            'gleisbett': {'tags': {'landuse': ['railway', 'industrial']}},
            'highway': {'tags': {'highway': ['footway', 'sideway', 'sidewalk', 'pedestrian', 'unclassified', 'construction']}},
            'place': {'tags': {'place': ['neighbourhood', 'quarter', 'suburb', 'residential', 'commercial', 'city_block']}},
            'man_made': {'tags': {'man_made': ['bridge', 'viaduct']}},
            'garden': {'tags': {'leisure': 'garden'}},

        },

        drawing_kwargs = {
            'background': {'fc': '#69a6bf', 'ec': '#dadbc1', 'zorder': -1},
            'perimeter': {'fc': '#bebe8e', 'ec': '#999999', 'lw': 6, 'zorder': 0},
            'green': {'fc': '#5dab4d', 'ec': '#89fa73', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#79a5ec', 'ec': '#94c6ee', 'lw': 0, 'zorder': 9},
            'streets': {'fc': '#F1E6D0', 'ec': '#2F3737', 'lw': 1.5, 'zorder': 4},
            'building': {'palette': ['#f58877', '#b35344', '#e37242', '#bd5022'], 'ec': '#2F3737', 'lw': 0.1, 'zorder': 9},
            'railway': {'fc': '#a2c2db', 'ec': '#FF0000', 'alpha': 1, 'lw': 0, 'zorder': 8},
            'forest': {'fc': '#427a36', 'ec': '#7a8a57', 'lw': 0, 'zorder': 1},
            'agriculture': {'fc': '#345e2b', 'ec': '#647031', 'lw': 0, 'zorder': 1},
            'developingLand': {'fc': '#315c24', 'ec': '#2F3737', 'lw': 0, 'zorder': 8},
            'sportstuff': {'fc': '#50bf0f', 'ec': '#ffffff', 'lw': 0.3, 'zorder': 8},
            'parkplatz': {'fc': '#42423a', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 3},
            'gleisbett': {'fc': '#7a7649', 'ec': '#32512b', 'lw': 0, 'zorder': 7},
            'cemeterystuff': {'fc': '#7BAE82', 'ec': '#2F3737', 'lw': 0, 'zorder': 9},
            'highway': {'fc': '#46693b', 'ec': '#ffffff', 'lw': 0, 'zorder': 10},
            'place': {'fc': '#819c78', 'ec': '#ffffff', 'lw': 0, 'zorder': 6},
            'man_made': {'fc': '#b52812', 'ec': '#ffffff', 'lw': 0, 'zorder': 11},
            'garden': {'fc': '#a9d1a9', 'ec': '#8ab58a', 'lw': 1, 'zorder': 1},

'coastline':{
    'file_location':'/home/bnb/Documents/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
    'buffer':100000,
    'circle':False
},

        },
        osm_credit = {'color': '#3b4545'}
)

ax.autoscale()

print("savefig")

plt.savefig('map.png', dpi=200)

