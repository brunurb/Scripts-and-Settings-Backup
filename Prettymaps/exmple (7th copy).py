from ridge_map import RidgeMap
from ridge_map import FontManager
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import mplcyberpunk
# Register fonts from local font files
font_prop = fm.FontProperties(fname="/media/bnb/32GB/Apps/Fonts/Abel-Regular.ttf")
# Based on the lower left corner of the incoming area 、 Latitude and longitude of the upper right corner
# To get the original elevation data and draw a ridge map
# If you have “ Special Internet skills ”, The waiting time for this step will be short

#plt.style.use("cyberpunk")

# initialization

font = FontManager('https://github.com/google/fonts/raw/main/ofl/uncialantiqua/UncialAntiqua-Regular.ttf')

# Get elevation data online http://bboxfinder.com/#0.000000,0.000000,0.000000,0.000000

rm = RidgeMap(bbox=(174.534302,-37.129666,175.253906,-36.580247), font=font.prop)

values = rm.get_elevation_data(num_lines=100)
rm.plot_map(values=rm.preprocess(values=values, lake_flatness=2, water_ntile=10, vertical_ratio=240),
            label="NZ",
            label_y=0.85,
            label_x=0.7,
            label_size=60,
            linewidth=2,
            line_color=plt.get_cmap('tab20'),
           #line_color=plt.style.use("cyberpunk")
            kind='elevation')

mplcyberpunk.make_lines_glow()
mplcyberpunk.add_underglow()

print("savefig")
plt.savefig('NZ.png', dpi=200, metadata=None)
plt.savefig('NZ.svg', metadata=None)

