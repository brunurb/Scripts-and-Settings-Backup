from ridge_map import RidgeMap
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
# Register fonts from local font files
font_prop = fm.FontProperties(fname="/media/bnb/32GB/Apps/Fonts/Abel-Regular.ttf")
# Based on the lower left corner of the incoming area 、 Latitude and longitude of the upper right corner
# To get the original elevation data and draw a ridge map
# If you have “ Special Internet skills ”, The waiting time for this step will be short

# initialization
rm = RidgeMap(bbox=(5.889,34.071,20.303,45.997),
font=font_prop)
# Get elevation data online
values = rm.get_elevation_data(num_lines=200, viewpoint='south')

values = rm.preprocess(values=values,
water_ntile=10,
vertical_ratio=240)
rm.plot_map(values, label="Italia", line_color='black', background_color='white')
print("savefig")
plt.savefig(' chartitalia.png', dpi=200)
plt.savefig('mapitalia.svg')
