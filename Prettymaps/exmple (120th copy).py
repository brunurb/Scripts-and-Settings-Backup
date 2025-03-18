# Prettymaps
from prettymaps import *
# Vsketch
import vsketch
# OSMNX
import osmnx as ox
# Matplotlib-related
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
# Shapely
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union

def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(10)
    return layers

fig, ax = plt.subplots(figsize = (10, 7.5), constrained_layout = True)

layers = plot(
    'Neighbourhood, Nova Oeiras',
    
    rotation = 180,

    ax = ax,
    
    postprocessing = postprocessing,

    layers = {
            'perimeter': {
                'width': .5
            },
            'streets': {
                'width': {
                    #'motorway': 8,
                    'trunk': 4,
                    'primary': 4,
                    'secondary': 3,
                    'tertiary': 2,
                    'residential': 1,
                    #'living_street': 3,
                    'pedestrian': .5,
                    'footway': .5,
                    #'track': 1,
                    #'bridleway': 1
                }
            },
            'building': {'tags': {'building': True}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'}},
        },
        drawing_kwargs = {
            'background': {'fc': '#64B96A', 'ec': '#EFE7EB', 'hatch': '.', 'zorder': -1},
            'perimeter': {'fc': '#e3d4ce', 'ec': '#fcebb4', 'lw': 3, 'hatch': '..', 'hatch_c': '#EFE7EB',  'zorder': 0},
            'green': {'fc': '#AABD8C', 'ec': '#2F3737', 'hatch_c': '#b3cfa5', 'hatch': 'oooooo', 'lw': 0, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'hatch': 'ooo...', 'hatch_c': '#80bed9', 'lw': 0, 'zorder': 2},
            'streets': {'fc': '#3b4545', 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#a0d590', '#d58344', '#d4a72b', '#5382ac'], 'ec': '#2F3737', 'hatch_c': '#b3504f', 'lw': .2, 'zorder': 4}, #'hatch': 'ooo...', 
        },

      osm_credit = {'x': 0.1, 'y': -0.02, 'color': '#2F3737'} 

)

print("savefig")

plt.savefig('map.png', dpi=200)
#plt.savefig('../prints/rome.svg')
