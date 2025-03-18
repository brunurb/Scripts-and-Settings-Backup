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
    (42.3640,-71.0585),
    radius = 1700,
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
            'parkplatz': {'circle': False,'tags': {'amenity': ['parking'], 'aeroway': ['apron', 'runway', 'taxiway']}},
            'gleisbett': {'circle': False,'tags': {'landuse': ['railway', 'industrial']}},
            'highway': {'circle': False,'tags': {'highway': ['unclassified', 'construction']}},
            'place': {'circle': False,'tags': {'place': ['neighbourhood', 'quarter', 'suburb', 'residential', 'commercial', 'city_block']}},
            'man_made': {'circle': False,'tags': {'man_made': ['bridge', 'viaduct']}},
            'garden': {'circle': False,'tags': {'leisure': 'garden'}},
            'motorway': {'circle': False,'tags': {'highway': ['motorway']}},
            'primary': {'circle': False,'tags': {'highway': ['primary']}},
            'service': {'circle': False,'tags': {'highway': ['service']}},
            'trunk': {'circle': False,'tags': {'highway': ['trunk']}},
            'secondary': {'circle': False,'tags': {'highway': ['secondary']}},
            'tertiary': {'circle': False,'tags': {'highway': ['tertiary']}},
            'residential': {'circle': False,'tags': {'highway': ['residential']}},
            'living_street': {'circle': False,'tags': {'highway': ['living_street']}},
            'pedestrian': {'circle': False,'tags': {'highway': ['pedestrian']}},
            'footway': {'circle': False,'tags': {'highway': ['footway']}},
            'sideway': {'circle': False,'tags': {'highway': ['sideway']}},
            'track': {'circle': False,'tags': {'highway': ['track']}},
            'bridleway': {'circle': False,'tags': {'highway': ['bridleway']}},
            'cycleway': {'circle': False,'tags': {'highway': ['cycleway']}},
            'path': {'circle': False,'tags': {'highway': ['path']}},
        },

        drawing_kwargs = {
            'background': {'fc': '#2A2A3A', 'ec': '#2A2A3A', 'zorder': -1},
            'perimeter': {'fc': '#2A2A3A', 'ec': '#2A2A3A', 'lw': 4, 'zorder': 0},
            'green': {'fc': '#5C7A56', 'ec': '#80AC40', 'lw': 0.5, 'zorder': 1},
            'water': {'fc': '#8BD0BA', 'ec': '#38607C','hatch': '...', 'hatch_c': '#38607C', 'lw': 0, 'zorder': 1},
            'streets': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 1, 'zorder': 16},
            'building': {'fc': '#523C4E', 'ec': '#D44E52', 'lw': 0.5, 'zorder': 15},
            'forest': {'fc': '#80AC40', 'ec': '#80AC40', 'lw': 0.5, 'zorder': 1},
            'agriculture': {'fc': '#B27E56', 'ec': '#B27E56', 'lw': 0.5, 'zorder': 1},
            'developingLand': {'fc': '#523C4E', 'ec': '#523C4E', 'lw': 0.5, 'zorder': 8},
            'sportstuff': {'fc': '#97E196', 'ec': '#074050', 'lw': 0.5, 'zorder': 8},
            'gleisbett': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.5, 'zorder': 7},
            'cemeterystuff': {'fc': '#B27E56', 'ec': '#B27E56', 'lw': 0.5, 'zorder': 14},
            'place': {'fc': '#FFCC68', 'ec': '#FFCC68', 'lw': 0.1, 'zorder': 6},
            'man_made': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 2, 'zorder': 19},
            'garden': {'fc': '#80AC40', 'ec': '#80AC40', 'lw': 1, 'zorder': 1},
            'railway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 12},
            'parkplatz': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.5, 'zorder': 14},
            'highway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.5, 'zorder': 18},
            'motorway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 18},
            'primary': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'service': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'trunk': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'secondary': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'tertiary': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'residential': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'living_street': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'pedestrian': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'footway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'sideway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'track': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'bridleway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'cycleway': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'path': {'fc': '#D44E52', 'ec': '#2A2A3A', 'lw': 0.1, 'zorder': 17},
            'coastline': {'fc': '#8BD0BA', 'ec': '#38607C','hatch': '...', 'hatch_c': '#38607C', 'lw': 0, 'zorder': 2}
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

