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



dilate = 0
doCircle = False

layers = plot(
    (38.74297,-9.15822),
    radius = 900,

    ax = ax,





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
            'building': {'tags': {'building': True}, 'union': False,'circle': doCircle, 'dilate': dilate},
            'water': {'tags': {'natural': ['water', 'bay', 'wetland'], 'waterway': ['ditch', 'stream', 'weir'], 'landuse': ['basin', 'reservoir'], 'water': True},'circle': doCircle, 'dilate': dilate},
            'green': {'tags': {'landuse': ['grass', 'allotments', 'village_green', 'allotments', 'nature_reserve', 'recreation_ground', 'cemetery', 'meadow'], 'natural': ['island', 'grassland', 'scrub'], 'leisure': ['park', 'garden', 'sports_centre', 'playground']},'circle': doCircle, 'dilate': dilate},
            'cemeterystuff': {'tags': {'landuse': ['cemetery']},'circle': doCircle, 'dilate': dilate},
            'railway': {'custom_filter': '["railway"~"rail|light_rail|subway|tram|narrow_gauge"]', 'width': 2,'circle': doCircle, 'dilate': dilate},
            'forest': {'tags': {'landuse': ['forest'], 'natural': ['wood']},'circle': doCircle, 'dilate': dilate},
            'agriculture': {'tags':{'landuse': ['farmland']},'circle': doCircle, 'dilate': dilate},
            'developingLand': {'tags': {'landuse': ['brownfield', 'greenfield', 'construction', 'quarry', 'landfill']},'circle': doCircle, 'dilate': dilate},
            'sportstuff': {'tags': { 'leisure': ['pitch', 'track'] },'circle': doCircle, 'dilate': dilate},
            'parkplatz': {'tags': {'amenity': ['parking'], 'aeroway': ['apron', 'runway', 'taxiway']},'circle': doCircle, 'dilate': dilate},
            'gleisbett': {'tags': {'landuse': ['railway', 'industrial']},'circle': doCircle, 'dilate': dilate},
            'highway': {'tags': {'highway': ['footway', 'sideway', 'sidewalk', 'pedestrian', 'unclassified', 'construction']},'circle': doCircle, 'dilate': dilate},
            'place': {'tags': {'place': ['neighbourhood', 'quarter', 'suburb', 'residential', 'commercial', 'city_block']},'circle': doCircle, 'dilate': dilate},
            'man_made': {'tags': {'man_made': ['bridge', 'viaduct']},'circle': doCircle, 'dilate': dilate},


        },

        drawing_kwargs = {
            'background': {'fc': '#64805b', 'ec': '#dadbc1', 'zorder': -1},
            'perimeter': {'fc': '#64805b', 'ec': '#b2b6b7', 'lw': 0, 'zorder': 0},
            'green': {'fc': '#5dab4d', 'ec': '#89fa73', 'lw': 1, 'zorder': 3},
            'water': {'fc': '#79a5ec', 'ec': '#94c6ee', 'lw': 0, 'zorder': 9},
            'streets': {'fc': '#f2d8bf', 'lw': 0, 'zorder': 11},
            'building': {'palette': ['#f58877', '#b35344', '#e37242', '#bd5022'], 'lw': 0.1, 'zorder': 9},
            'railway': {'fc': '#a2c2db', 'ec': '#FF0000', 'alpha': 1, 'lw': 0, 'zorder': 8},
            'forest': {'fc': '#427a36', 'ec': '#7a8a57', 'lw': 0, 'zorder': 5},
            'agriculture': {'fc': '#345e2b', 'ec': '#647031', 'lw': 0, 'zorder': 1},
            'developingLand': {'fc': '#315c24', 'ec': '#2F3737', 'lw': 0, 'zorder': 8},
            'sportstuff': {'fc': '#50bf0f', 'ec': '#ffffff', 'lw': 0.3, 'zorder': 8},
            'parkplatz': {'fc': '#42423a', 'ec': '#ffffff', 'lw': 0.1, 'zorder': 4},
            'gleisbett': {'fc': '#7a7649', 'ec': '#32512b', 'lw': 0, 'zorder': 7},
            'cemeterystuff': {'fc': '#7BAE82', 'ec': '#2F3737', 'lw': 0, 'zorder': 9},
            'highway': {'fc': '#46693b', 'ec': '#ffffff', 'lw': 0, 'zorder': 11},
            'place': {'fc': '#819c78', 'ec': '#ffffff', 'lw': 0, 'zorder': 2},
            'man_made': {'fc': '#b52812', 'ec': '#ffffff', 'lw': 0, 'zorder': 10},

'coastline':{'circle': False,
    'file_location':'/media/bbb/32GB/prettymaps/Assets/water-polygons-split-4326/water_polygons.shp',
    'dilate':True,
    'buffer':100000,
},

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
    bbox=dict(fc='#2e3561', ec='white', boxstyle='square,pad=0.5'),
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

