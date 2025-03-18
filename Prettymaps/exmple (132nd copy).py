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


fig, ax = plt.subplots(figsize = (15, 20), constrained_layout = True)
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
            'highway': {'tags': {'highway': ['unclassified', 'construction']}},
            'place': {'tags': {'place': ['neighbourhood', 'quarter', 'suburb', 'residential', 'commercial', 'city_block']}},
            'man_made': {'tags': {'man_made': ['bridge', 'viaduct']}},
            'garden': {'tags': {'leisure': 'garden'}},
            'streets': {'motorway', 'motorway_link', 'service', 'trunk', 'primary', 'secondary', 'tertiary', 'residential', 'living_street', 'pedestrian', 'footway', 'sideway', 'track', 'bridleway', 'cycleway', 'path', 'unclassified', 'construction'},

        },

        drawing_kwargs = {
            'background': {'fc': '#e8dfdf', 'ec': '#0a0100', 'zorder': -1},
            'perimeter': {'fc': '#f0f0f0', 'ec': '#5c1b11', 'lw': 4, 'zorder': 0},
            'green': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 1},
            'water': {'fc': '#f0f0f0', 'ec': '#0a0100', 'lw': 0, 'zorder': 9},
            'streets': {'fc': '#946d6d', 'ec': '#cca9a9', 'lw': 2, 'zorder': 12},
            'building': {'fc': '#e6b3b3', 'ec': '#6e2222', 'lw': 0.5, 'zorder': 15},
            'railway': {'fc': '#946d6d', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 12},
            'forest': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 1},
            'agriculture': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 1},
            'developingLand': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 8},
            'sportstuff': {'fc': '#f0f0f0', 'ec': '#ffffff', 'lw': 0.5, 'zorder': 8},
            'parkplatz': {'fc': '#f0f0f0', 'ec': '#ffffff', 'lw': 0.5, 'zorder': 3},
            'gleisbett': {'fc': '#ffb3b3', 'ec': '#704444', 'lw': 0.5, 'zorder': 7},
            'cemeterystuff': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 14},
            'highway': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 10},
            'place': {'fc': '#f0f0f0', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 6},
            'man_made': {'fc': '#b52812', 'ec': '#5c1b11', 'lw': 0.5, 'zorder': 16},
            'garden': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 1, 'zorder': 1},

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

