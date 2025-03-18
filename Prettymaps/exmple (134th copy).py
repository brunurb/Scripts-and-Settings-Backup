from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union





fig, ax = plt.subplots(figsize = (15, 20), constrained_layout = True)


layers = plot(
    (38.6985,-9.1866), radius = 4000,
    ax = ax,
    layers = {
            'perimeter': {},
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
            #'streets': {'motorway', 'motorway_link', 'service', 'trunk', 'primary', 'secondary', 'tertiary', 'residential', 'living_street', 'pedestrian', 'footway', 'sideway', 'track', 'bridleway', 'cycleway', 'path', 'unclassified', 'construction'},

        },

        drawing_kwargs = {
            'background': {'fc': '#c8d2e6', 'ec': '#2d4a80', 'zorder': -1},
            'perimeter': {'fc': '#f0f0f0', 'ec': '#c5d3ed', 'lw': 4, 'zorder': 0},
            'green': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 1},
            'water': {'fc': '#f0f0f0', 'ec': '#0a0100', 'lw': 0, 'zorder': 9},
            'streets': {'fc': '#c5d3ed', 'ec': '#2d4a80', 'lw': 1, 'zorder': 12},
            'building': {'fc': '#ff6200', 'ec': '#faeee6', 'lw': 0.5, 'zorder': 15},
            'railway': {'fc': '#c5d3ed', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 12},
            'forest': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 1},
            'agriculture': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 1},
            'developingLand': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 8},
            'sportstuff': {'fc': '#f0f0f0', 'ec': '#ffffff', 'lw': 0.5, 'zorder': 8},
            'parkplatz': {'fc': '#f0f0f0', 'ec': '#ffffff', 'lw': 0.5, 'zorder': 3},
            'gleisbett': {'fc': '#2d4a80', 'ec': '#704444', 'lw': 0.5, 'zorder': 7},
            'cemeterystuff': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 14},
            'highway': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 0.5, 'zorder': 10},
            'place': {'fc': '#f0f0f0', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 6},
            'man_made': {'fc': '#c5d3ed', 'ec': '#2d4a80', 'lw': 2, 'zorder': 16},
            'garden': {'fc': '#f0f0f0', 'ec': '#704444', 'lw': 1, 'zorder': 1},

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

