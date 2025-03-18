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
    (40.6971,-73.9796),
    radius = 600,
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
            'background': {'ec': '#df9ff5', 'zorder': -1},
            'perimeter': {'ec': '#df9ff5', 'lw': 0, 'zorder': 0},
            'streets': {'ec': '#fffd01', 'lw': 0.1, 'zorder': 12},
            'highway': {'ec': '#e359ff', 'lw': 0.5, 'zorder': 17},
            'man_made': {'ec': '#fffd01', 'lw': 0.2, 'zorder': 18},
            'motorway': {'fc': '#ff36fc', 'ec': '#ff78fd', 'lw': 2, 'zorder': 17},
            'primary': {'fc': '#e5ff00', 'ec': '#f0ff69', 'lw': 2, 'zorder': 17},
            'service': {'fc': '#ff1cfb', 'ec': '#ff78fd', 'lw': 2, 'zorder': 17},
            'trunk': {'fc': '#C00050', 'ec': '#b34271', 'lw': 2, 'zorder': 17},
            'secondary': {'fc': '#FF2636', 'ec': '#ff8790', 'lw': 2, 'zorder': 17},
            'tertiary': {'fc': '#4064af', 'ec': '#7182a6', 'lw': 2, 'zorder': 17},
            'residential': {'fc': '#73ff00', 'ec': '#b8fa82', 'lw': 2, 'zorder': 17},
            'living_street': {'fc': '#7AFF01', 'ec': '#bfff85', 'lw': 2, 'zorder': 17},
            'pedestrian': {'fc': '#FFFD01', 'ec': '#fffe91', 'lw': 2, 'zorder': 17},
            'footway': {'fc': '#FF015B', 'ec': '#ff8ab3', 'lw': 2, 'zorder': 17},
            'sideway': {'fc': '#0020FF', 'ec': '#8090ff', 'lw': 2, 'zorder': 17},
            'track': {'fc': '#FF7C00', 'ec': '#ffbc7d', 'lw': 2, 'zorder': 17},
            'bridleway': {'fc': '#FA00FF', 'ec': '#fc6eff', 'lw': 2, 'zorder': 17},
            'cycleway': {'fc': '#56F373', 'ec': '#c2ffcd', 'lw': 2, 'zorder': 17},
            'path': {'fc': '#ffd500', 'ec': '#ffefa1', 'lw': 2, 'zorder': 17},

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
    bbox=dict(fc='#01051c', ec='white', boxstyle='square,pad=0.5'),
    fontproperties = fm.FontProperties(fname='/home/bnb/Documents/prettymaps/Assets/Fonts/PermanentMarker-Regular.ttf'),
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
    fontproperties = fm.FontProperties(fname='/home/bnb/Documents/prettymaps/Assets/Fonts/RacingSansOne-Regular.ttf'),
    zorder = 20,
    transform=ax.transAxes
)
"""

print("saving map image ...")

plt.savefig('temp.png', dpi=200)
plt.savefig('map.svg')

"""
print("merging ...")
# here starts the assembling using svgutils 
sc.Figure("2283", "2283", 
    sc.Panel(sc.SVG("map.svg").scale(1).move(0,0)),
    sc.Panel(sc.SVG("SPREADSHIRT60x60FRAME.svg").scale(1).move(0,0))
    ).save("compose.svg")
SVG('compose.svg')
print("... ...")
print("... DONE!!!")
"""
