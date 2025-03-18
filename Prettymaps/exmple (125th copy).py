"""
References

* https://prettymaps.readthedocs.io/en/latest/prettymaps.html#module-prettymaps
* https://nbviewer.org/github/marceloprates/prettymaps/blob/main/notebooks/examples.ipynb
* https://fonts.google.com/specimen/Permanent+Marker
"""
from prettymaps import plot
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm


fig, ax = plt.subplots(figsize=(40, 40))

dilate = 80
palette = ['#FFEDDF', '#E7A89C']

layers = plot(
        (38.69221,-9.31253), radius = 4000,
    ax=ax,
    layers={
        'perimeter': {
            'circle': False,
            'dilate': dilate
        },
        'streets': {
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
                'footway': 1,
            },
            'circle': False,
            'dilate': dilate
        },
        'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False, 'circle': False, 'dilate': dilate},
        'water': {'tags': {'natural': ['water', 'bay']},
                  'circle': False, 'dilate': dilate},
        'green': {'tags': {'landuse': 'grass', 'natural': ['island', 'wood'], 'leisure': 'park'},
                  'circle': False, 'dilate': dilate},
    },
    drawing_kwargs={
        'background': {'fc': '#FFFFFF', 'ec': '#FFFFFF', 'zorder': -1},
        'perimeter': {'fc': '#F7F3F5', 'ec': '#2F3737', 'lw': 3, 'hatch': 'ooo...', 'hatch_c': '#EFE7EB', 'zorder': 0},
        'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
        'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'streets': {'fc': '#797979', 'lw': 0, 'zorder': 3},
        'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
    },
    osm_credit={'color': '#797979'},
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax - xmin, ymax - ymin
ax.set_xlim(xmin - .06 * dx, xmax + .06 * dx)
ax.set_ylim(ymin - .06 * dy, ymax + .06 * dy)

# Draw left text
ax.text(
    xmin - .06 * dx, ymin + .2 * dy,
    'Vila de Oeiras e Nova Oeiras',
    color='#2F3737',
    rotation=90,
    fontproperties=fm.FontProperties(fname='./PermanentMarker-Regular.ttf', size=80),
)
# Draw top text
ax.text(
    xmax - .45 * dx, ymax + .02 * dy,
    "OEIRAS 2022, PT",
    color='#2F3737',
    fontproperties=fm.FontProperties(fname='./PermanentMarker-Regular.ttf', size=80),
)

plt.savefig('map.png')
plt.savefig('map.svg')
