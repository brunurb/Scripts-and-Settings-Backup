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

dilate = 100
doCircle = False

layers = plot(
    'Santa Maria Maior (6427496)',
    # Or coordinates  (38.7179,-9.1662)

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
            'building': {'tags': {'building': True}, 'union': True,'circle': doCircle, 'dilate': dilate},
            'water': {'tags': {'natural': ['water', 'bay', 'wetland'], 'waterway': ['ditch', 'stream', 'weir'], 'landuse': ['basin', 'reservoir'], 'water': True},'circle': doCircle, 'dilate': dilate},
            'green': {'tags': {'landuse': ['grass', 'allotments', 'village_green', 'allotments', 'nature_reserve', 'recreation_ground', 'cemetery', 'meadow'], 'natural': ['island', 'grassland', 'scrub'], 'leisure': ['park', 'garden', 'sports_centre', 'playground']},'circle': doCircle, 'dilate': dilate},
            'cemeterystuff': {'tags': {'landuse': ['cemetery']},'circle': doCircle, 'dilate': dilate},
            'railway': {'custom_filter': '["railway"~"rail|light_rail|subway|tram"]', 'width': 2,'circle': doCircle, 'dilate': dilate},
            'forest': {'tags': {'landuse': ['forest'], 'natural': ['wood']},'circle': doCircle, 'dilate': dilate},
            'agriculture': {'tags':{'landuse': ['farmland']},'circle': doCircle, 'dilate': dilate},
            'developingLand': {'tags': {'landuse': ['brownfield', 'greenfield', 'construction', 'landfill']},'circle': doCircle, 'dilate': dilate},
            'sportstuff': {'tags': { 'leisure': ['pitch', 'track'] },'circle': doCircle, 'dilate': dilate},
            'parkplatz': {'tags': {'amenity': ['parking'], 'aeroway': ['apron', 'runway', 'taxiway']},'circle': doCircle, 'dilate': dilate},
            'gleisbett': {'tags': {'landuse': ['railway', 'industrial']},'circle': doCircle, 'dilate': dilate}
        },
        drawing_kwargs = {
            'background': {'fc': '#bad2f5', 'ec': '#a3b9d9', 'hatch': '///', 'zorder': -1},
            'perimeter': {'fc': '#ffe8c4', 'ec': '#383838', 'lw': 3, 'zorder': 0},
            'green': {'fc': '#AABD8C', 'ec': '#2F3737', 'lw': 0, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'lw': 0, 'zorder': 3},
            'streets': {'fc': '#3b4545', 'lw': 0, 'zorder': 4},
            'building': {'palette': ['#bd6337', '#eb6a4d'], 'ec': '#2F3737', 'lw': 0, 'zorder': 3},
            'railway': {'fc': '#a8a8a8', 'ec': '#FF0000', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'forest': {'fc': '#228b22', 'ec': '#2F3737', 'lw': 0, 'zorder': 1},
            'agriculture': {'fc': '#f5d6a8', 'ec': '#2F3737', 'lw': 0, 'zorder': 1},
            'developingLand': {'fc': '#898878', 'ec': '#2F3737', 'lw': 0, 'zorder': 1},
            'sportstuff': {'fc': '#66A457', 'ec': '#32512b', 'lw': 0.3, 'zorder': 1},
            'parkplatz': {'fc': '#a3a3a3', 'ec': '#32512b', 'lw': 0, 'zorder': 1},
            'gleisbett': {'fc': '#ebdbe8', 'ec': '#32512b', 'lw': 0, 'zorder': 1},
            'cemeterystuff': {'fc': '#7BAE82', 'ec': '#2F3737', 'lw': 0, 'zorder': 1},
        },
        osm_credit = {'color': '#3b4545'}
)

print("savefig")

plt.savefig('map.png', dpi=200)
plt.savefig('map.svg')
