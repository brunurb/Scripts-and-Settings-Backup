from prettymaps import *
import vsketch
import osmnx as ox
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union

fig, ax = plt.subplots(figsize = (20, 20), constrained_layout = True)

dilate = 0

map = plot(
  #Centre the map roughly on oeiras  
  (38.6867,-9.3213),
  #Set radius for the map
  radius = 1500,
  ax=ax,
  #Name and select the various layers we want on the map
  #We want a square map so ensure that we're not querying for data in a circle
  layers = {
      #we want a square layout, so 
      'perimeter': {'circle': False, 'dilate': dilate },
      'river': {'tags': {'natural': 'water'}, 'circle': False, 'dilate': dilate },
      'rail': {'tags': {'railway': 'rail'}, 'circle': False, 'dilate': dilate },
      'station': {'tags': {'building': 'train_station'} },
      'building': {'tags': {'building': True}, 'circle': False, 'dilate': dilate },
      'roads': {'tags': {'bridge': 'yes'}, 'circle': False, 'dilate': dilate },
      'parks': {'tags': {'landuse': 'grass', 'leisure': 'park'}, 'circle': False, 'dilate': dilate},
      'recreation': {'tags': {'landuse': 'recreation_ground'}, 'circle': False, 'dilate': dilate },     
      'allotments': { 'tags': {'landuse': 'allotments'}, 'circle': False, 'dilate': dilate },   
      'parking': {'tags': {'amenity': 'parking'}, 'circle': False, 'dilate': dilate },
      'paths': {'tags': {'highway': ['pedestrian', 'footway'] }, 'circle': False, 'dilate': dilate },
      'residential': {'tags': {'landuse': 'residential'}, 'circle': False, 'dilate': dilate },
      'highlights': {'tags': {'building': ['church', 'school'], 'tourism': ['museum', 'attraction'], 'amenity': ['theatre', 'cinema', 'post_office', 'townhall', 'place_of_worship'], 'water': 'basin'}, 'union': False, 'circle': False, 'dilate': dilate}               
  },
  #Style the individual layers
  drawing_kwargs = {
      #specify the background colour of the map
      'background': { 'fc': '#c7bfad', 'lw': 1 },
      'perimeter': {'fill': False, 'zorder': 0},
      'river': {'fc': '#bcb7aa', 'ec': '#342c28', 'hatch': '......', 'hatch_c': '#332c29', 'zorder': 1},
      'building': {'fc': '#847d77', 'ec': '#342c28', 'lw': .5, 'zorder': 2},
      'parks': {'fc': '#b8ad9b', 'ec': '#aca59f', 'lw': 1, 'hatch': '......', 'hatch_c': '#b3a497'},
      'recreation': {'fc': '#c7bfad', 'ec': '#aca59f', 'lw': 1, 'hatch': '......', 'hatch_c': '#b3a497'},
      'allotments': {'fc': '#b8ad9b', 'ec': '#aca59f', 'lw': 1, 'hatch': '......', 'hatch_c': '#b3a497'},
      'station': {'fc': '#342c28', 'lw': .5, 'zorder': 3},
      'roads': { 'fc': '#c7bfad', 'ec': '#c7bfad', 'lw': 1, 'zorder': 4 },     
      'rail': {'fc': '#000000', 'lw': 1, 'ec': '#342c28', 'zorder': 3},
      'parking': {'fc': '#847d77', 'ec': '#aca59f'},
      'paths': {'fc': '#c7bfad', 'lw': .5, 'ec': '#c7bfad', 'zorder': 3},
      'residential': {'fc': '#cac0aa', 'ec': '#aca59f', 'lw': 1, 'zorder': 1}, 
      'highlights': {'fc': '#342c28', 'lw': .5, 'zorder': 3}            
  },
  osm_credit = False
)

# Set bounds
xmin, ymin, xmax, ymax = map['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
ax.set_ylim(ymin-.06*dy, ymax+.06*dy)

#Add the title, in a victorian font (https://www.1001fonts.com/victoriantext-font.html)
ax.text(
    xmin+.0001*dx, ymax+.02*dy,
    "Lisboa, Portugal - by brunurb",
    color = '#2F3737',
    size = 50,
    zorder = 6,
    fontproperties = fm.FontProperties(fname = '/home/bnb/Desktop/example/2/assets/VictorianText.ttf', size = 50),  
)

#Add attributions
ax.text(
    xmin+.0001*dx, ymin-.06*dy,
    "Made by Leigh Dodds (2022). Inspired by J. H Cotterell (1852). Data © OpenStreetMap contributors",
    color = '#2F3737',
    size = 20,
    zorder = 6  
)

print("savefig")

plt.savefig('lx.png')
plt.savefig('LX.svg')
