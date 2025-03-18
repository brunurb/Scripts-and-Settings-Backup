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

fig, ax = plt.subplots(figsize = (10, 13), constrained_layout = True)
fig.patch.set_facecolor('#F9F8F8')

def postprocessing(layers):
    layers['perimeter'] = layers['perimeter'].buffer(20)
    return layers



layers = plot(
    'Alcântara, Lisbon, Portugal',
    
    ax = ax,
    
    postprocessing = postprocessing,

        layers = {
            'perimeter': {},
            'streets': {
                'width': {
                    'trunk': 6,
                    'primary': 6,
                    'secondary': 5,
                    'tertiary': 4,
                    'residential': 3.5,
                    'pedestrian': 3,
                    'footway': 3,
                    'path': 3,
                }
            },
            'building': {'tags': {'building': True, 'leisure': ['track', 'pitch']}, 'union': False},
            'water': {'tags': {'natural': ['water', 'bay']}},
            'park': {'tags': {'leisure': 'park'}},
            'forest': {'tags': {'landuse': 'forest'}},
            'garden': {'tags': {'leisure': 'garden'}},
        },
        drawing_kwargs = {
            'perimeter': {'fill': True, 'fc': '#bebe8e', 'ec': '#999999', 'lw': 0, 'zorder': 0},
            'park': {'fc': '#AABD8C', 'ec': '#87996b', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#78A58D', 'ec': '#658a76', 'lw': 1, 'zorder': 1},
            'garden': {'fc': '#a9d1a9', 'ec': '#8ab58a', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#92D5F2', 'ec': '#6da8c2', 'lw': 1, 'zorder': 2},
            'streets': {'fc': '#F1E6D0', 'ec': '#2F3737', 'lw': 1.5, 'zorder': 3},
            'building': {'palette': ['#BA2D0B', '#D5F2E3', '#73BA9B', '#F79D5C'], 'ec': '#2F3737', 'lw': 1, 'zorder': 4},
        },

        osm_credit = {'x': 0.3, 'y': -.1, 'color': '#2F3737'}
    )

ax.autoscale()

print("savefig")

plt.savefig('map.png', dpi=200)
#plt.savefig('../prints/rome.svg')
