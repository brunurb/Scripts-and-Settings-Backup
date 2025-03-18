# coding=utf8
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize = (12, 12), constrained_layout = True)

dilate = 25

# plot() ist die Funktion, die die Karte/plot erstellt
colored_map = plot(
    # Ort:
    (50.6598,6.6507),
    #"Gartenstraße 26, 53909 Zülpich", # oder (52.516272, 13.377722)
    # Radius Meter
    radius = 600,
    ax = ax,
    layers = {
            'perimeter': {'circle': False, 'dilate': dilate},
            # "streets{}" filtert und importiert verschiedenste Straßentypen
            'streets': {
                # nicht alle Straßentypen werden in die Karte übernommen, sondern nur die mit dem Merkmal/key "highway", hier im Filter angegeben werden
                'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway|track"]',
                # Mit "width{}" kann man anpassen, wie breit die Straßen auf der Karte dargestellt werden sollen. 
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'track': 1,
                    'footway': 1,
                },
                'circle': False,
                'dilate': dilate
            },
            # Add named layers here. Each layer will contain elements of the given tags.
            # Tags: https://wiki.openstreetmap.org/wiki/Map_features
            # Find tags for specific map parts at https://www.openstreetmap.org/edit (Account required!)
            'building': {
              'tags': {'building': True, 'landuse': 'construction'},
              'union': False,
              'circle': False,
              'dilate': dilate
            },
            'water_still': {
              'tags': {'natural': ['water'], 'water': ['ditch', 'pond', 'wastewater']},
              'circle': False,
              'dilate': dilate
            },
            'water_flowing': {
              'tags': {'natural': ['strait', 'spring'], 'waterway': ['river', 'stream']},
              'circle': False,
              'dilate': dilate
            },
            'green_used': {
              'tags': {'landuse': ['farmland', 'farmyard', 'orchard', 'allotments'], 'leisure': ['garden', 'park', 'pitch']},
              'circle': False,
              'dilate': dilate
            },
            'green_nature': {
              'tags': {'landuse': ['grass', 'meadow', 'village_green'], 'natural': ['wood', 'grassland']},
              'circle': False,
              'dilate': dilate
            },
            'green_extra': {
              'tags': {'landuse': ['forest'], 'natural': ['scrub']},
              'circle': False,
              'dilate': dilate
            },
            'living': {
              'tags': {'landuse': ['residential', 'industrial', 'education', 'commercial', 'landfill']},
              'circle': False,
              'dilate': dilate
            },
            'sportplatz': {
              'tags': {'sport': ['soccer']},
              'circle': False,
              'dilate': dilate
            }
        },
        # Hatches: https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch
        # Examples: https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html
        drawing_kwargs = {
            'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...',  'zorder': 0},
            'green_used': {'fc': '#D0F1BF', 'ec': '#2F3737', 'hatch': '///', 'hatch_c': '#b2e896', 'lw': 0, 'zorder': 1},
            'green_nature': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 0, 'zorder': 1},
            'green_extra': {'fc': '#479e4c', 'ec': '#2F3737', 'hatch': '///', 'hatch_c': '#4fb054', 'lw': 0, 'zorder': 1},
            'living': {'fc': '#F2F4CB', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
            'water_still': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': '///', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
            'water_flowing': {'fc': '#a1e3ff', 'ec': '#a1e3ff', 'lw': 1, 'zorder': 2},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
            'sportplatz': {'fc': '#ffb84d', 'ec': '#475657', 'hatch': '....', 'hatch_c': '#cc7a00', 'lw': 0, 'zorder': 4},
            # 'palette' gibt eine ganze Farbpalette für ein Objekt vor, als Liste in []
            'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
        },
        # Das Quellen-Attribut ist Standard bei Open Street Maps. AUch dem sog. "credit" kann eine individuelle Farbe zugewiesen werden
        osm_credit = False
)

# Set bounds
xmin, ymin, xmax, ymax = colored_map['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
#ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
#ax.set_ylim(ymin-.06*dy, ymax+.06*dy)

# Draw left text
ax.text(
    xmin+.01*dx, ymax-.015*dy,
    'Sinzenich, Zülpich',
    color = '#2F3737',
    fontproperties = fm.FontProperties(fname = '/home/bnb/Documents/prettymaps/Assets/Fonts/PermanentMarker-Regular.ttf', size = 35),
    in_layout = False
)

print("savefig")

plt.savefig('map.png', dpi=200)
plt.savefig('map.svg')
