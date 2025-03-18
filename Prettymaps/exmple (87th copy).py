from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union

dilate = 100

class Sketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        
        vsk.size("a4", landscape = True)

        global layers
        layers = plot(
            (38.7179,-9.1662), radius = 500,
            vsketch = vsk,
            layers = {
                'perimeter': {'circle': False, 'dilate': dilate},
                'streets': {
                    'width': {
                        'primary': 5,
                        'secondary': 4,
                        'tertiary': 3,
                        'residential': 2,
                        'footway': 1,
                    },
                    'circle': False,
                    'dilate': dilate
                },
                'building': {
                    'tags': {'building': True},
                    'union': False,
                    'circle': False,
                    'dilate': dilate
                },
                'green': {
                    'tags': {
                        'landuse': ['grass', 'village_green'],
                        'leisure': 'park'
                    },
                    'circle': False,
                    'dilate': dilate
                },
            },

            scale_x = .65,
            scale_y = -.65,

            drawing_kwargs = {
                'perimeter': {'draw': False},
                'streets': {'stroke': 1, 'fill': 1, 'penWidth': 2},
                'buildings': {'stroke': 2},
            },
        )

        vsk.save("barcelona-plotter.svg")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")

sketch = Sketch()
sketch.display()

