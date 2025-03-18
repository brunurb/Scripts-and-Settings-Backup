from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union
import svgutils.compose as sc
from IPython.display import SVG # /!\ note the 'SVG' function also in svgutils.compose

fig, ax = plt.subplots(figsize = (32, 32), constrained_layout = True)

dilate = 100
doCircle = False

layers = plot(
    (25.7764,-80.1947),
    radius = 2200,
    ax = ax,

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
    'file_location':'/media/bbb/32GB/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
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

        },

        drawing_kwargs = {
            'background': {'fc': '#5b8064', 'ec': '#5b8064', 'zorder': -1},
            'perimeter': {'fc': '#5b8064', 'zorder': 0},
            'green': {'palette': ['#64805b', '#5b8064', '#6e805b', '#7e805b', '#80725b'], 'lw': 0, 'zorder': 1},
            'water': {'fc': '#79a5ec', 'ec': '#94c6ee', 'lw': 0, 'zorder': 1},
            'streets': {'fc': '#f2d8bf', 'lw': 0, 'lw': 0, 'zorder': 16},
            'building': {'palette': ['#0099e6', '#12255a', '#f23814', '#dfb78b', '#b6c3c5'], 'lw': 0, 'zorder': 15},
            'forest': {'palette': ['#0099e6', '#12255a', '#f23814', '#dfb78b', '#b6c3c5'], 'lw': 0, 'zorder': 1},
            'agriculture': {'palette': ['#64805b', '#5b8064', '#6e805b', '#7e805b', '#80725b'], 'lw': 0, 'zorder': 1},
            'developingLand': {'palette': ['#64805b', '#5b8064', '#6e805b', '#7e805b', '#80725b'], 'lw': 0, 'zorder': 8},
            'sportstuff': {'palette': ['#64805b', '#5b8064', '#6e805b', '#7e805b', '#80725b'], 'lw': 0, 'zorder': 8},
            'cemeterystuff': {'palette': ['#64805b', '#5b8064', '#6e805b', '#7e805b', '#80725b'], 'lw': 0, 'zorder': 14},
            'place': {'palette': ['#0099e6', '#12255a', '#f23814', '#dfb78b', '#b6c3c5'], 'lw': 0, 'zorder': 6},
            'railway': {'fc': '#a2c2db', 'zorder': 12},
            'coastline': {'fc': '#79a5ec', 'ec': '#94c6ee', 'lw': 0, 'zorder': 2}
        },
        osm_credit = {'color': '#3b4545'}
)

"""
# LABEL TEXTO
ax.text(
    0.5, 0.09,
    'Sines',
    ha='center',
    va='top',
    fontsize=60,
    color='white',
    bbox=dict(fc='#42143e', ec='white', boxstyle='square,pad=0.5'),
    fontproperties = fm.FontProperties(fname='/media/bbb/32GB/prettymaps/Assets/Fonts/PermanentMarker-Regular.ttf'),
    zorder = 20,
    transform=ax.transAxes
)
ax.text(
    0.5, 0.067,
    '- . -',
    ha='center',
    va='top',
    fontsize=20,
    color='white',
    fontproperties = fm.FontProperties(fname='/media/bbb/32GB/prettymaps/Assets/Fonts/RacingSansOne-Regular.ttf'),
    zorder = 20,
    transform=ax.transAxes
)
"""

print("saving map image ...")

plt.savefig('map.png', dpi=200)
plt.savefig('map.svg')


print("merging ...")
# here starts the assembling using svgutils 
sc.Figure("2283", "2283", 
    sc.Panel(sc.SVG("map.svg").scale(1).move(0,0)),
    sc.Panel(sc.SVG("SPREADSHIRT60x60FRAME.svg").scale(1).move(0,0))
    ).save("compose.svg")
SVG('compose.svg')
print("... ...")
print("... DONE!!!")

