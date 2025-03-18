import matplotlib.pyplot as plt
import svgutils.compose as sc
from IPython.display import SVG # /!\ note the 'SVG' function also in svgutils.compose
import numpy as np


# here starts the assembling using svgutils 
sc.Figure("2700", "2700", 
    sc.Panel(sc.SVG("map.svg").scale(1).move(0,0)),
    sc.Panel(sc.SVG("MapBLANK.svg").scale(2).move(0,0))
    ).save("compose.svg")
SVG('compose.svg')

