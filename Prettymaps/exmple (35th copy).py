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
    (41.4036,2.1868),
    radius = 1500,
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
            'background': {'fc': '#42143e', 'ec': '#be1059', 'zorder': -1},
            'perimeter': {'fc': '#42143e', 'ec': '#be1059', 'lw': 4, 'zorder': 0},
            'green': {'fc': '#1c2837', 'ec': '#be1059', 'lw': 0.5, 'zorder': 1},
            'water': {'fc': '#42143e', 'ec': '#be1059','hatch': '...', 'hatch_c': '#be1059', 'lw': 0, 'zorder': 1},
            'streets': {'fc': '#42143e', 'ec': '#42143e', 'lw': 1, 'zorder': 16},
            'building': {'fc': '#4D004F', 'ec': '#C1115A', 'lw': 0.5, 'zorder': 15},
            'forest': {'fc': '#1c2837', 'ec': '#be1059', 'lw': 0.5, 'zorder': 1},
            'agriculture': {'fc': '#1c2837', 'ec': '#be1059', 'lw': 0.5, 'zorder': 1},
            'developingLand': {'fc': '#1c2837', 'ec': '#be1059', 'lw': 0.5, 'zorder': 8},
            'sportstuff': {'fc': '#42143e', 'ec': '#be1059', 'lw': 0.5, 'zorder': 8},
            'gleisbett': {'fc': '#42143e', 'ec': '#be1059', 'lw': 0.5, 'zorder': 7},
            'cemeterystuff': {'fc': '#42143e', 'ec': '#be1059', 'lw': 0.5, 'zorder': 14},
            'place': {'fc': '#1c2837', 'ec': '#be1059', 'lw': 0.1, 'zorder': 6},
            'man_made': {'fc': '#42143e', 'ec': '#be1059', 'lw': 2, 'zorder': 16},
            'garden': {'fc': '#1c2837', 'ec': '#be1059', 'lw': 1, 'zorder': 1},
            'railway': {'fc': '#0AFF52', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 12},
            'parkplatz': {'fc': '#1c2837', 'ec': '#3e597a', 'lw': 0.5, 'zorder': 14},
            'highway': {'fc': '#07EF5C', 'ec': '#FF5CFF', 'lw': 0.5, 'zorder': 17},
            'motorway': {'fc': '#00F7FF', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'primary': {'fc': '#53EBE4', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'service': {'fc': '#f0de16', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'trunk': {'fc': '#07EF5C', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'secondary': {'fc': '#bdf016', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'tertiary': {'fc': '#f03e16', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'residential': {'fc': '#3a16f0', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'living_street': {'fc': '#fad000', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'pedestrian': {'fc': '#42143e', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'footway': {'fc': '#f0de16', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'sideway': {'fc': '#f0de16', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'track': {'fc': '#07EF5C', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'bridleway': {'fc': '#1670f0', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'cycleway': {'fc': '#f09c16', 'ec': '#FF5CFF', 'lw': 0.1, 'zorder': 17},
            'path': {'fc': '#f01653', 'ec': '#051885', 'lw': 0.1, 'zorder': 17},
            'coastline': {'fc': '#42143e', 'ec': '#be1059','hatch': '...', 'hatch_c': '#be1059', 'lw': 0, 'zorder': 2}
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

