https://github.com/koenderks/rcityviews?tab=readme-ov-file

# Start R
sudo -i R

#Load CityViews
library(rcityviews)


#Fetch map
 p <- cityview(name = "Santarem", theme = "modern", legend = TRUE, license = FALSE, zoom = 1, border = "bbox", places = 20)

#save image
ggplot2::ggsave(filename = "/home/b/Desktop/Santarem.png", plot = p, height = 500, width = 500, units = "mm", dpi = 100)

#or PDF or SVG
ggplot2::ggsave(filename = "/home/b/Desktop/Santarem.pdf", plot = p, height = 500, width = 500, units = "mm")


In addition to the ten pre-specified themes, the package provides full flexibility to customize the theme by providing a named list. This is demonstrated in the code block below.

# For example: black, beige and white theme, streets only
myTheme <- list(
  colors = list(
    background = "#232323",
    water = "#232323",
    landuse = "#232323",
    contours = "#232323",
    streets = "#d7b174",
    rails = c("#d7b174", "#232323"),
    buildings = "#232323",
    text = "#ffffff",
    waterlines = "#232323"
  ),
  font = list(
    family = "serif",
    face = "bold",
    scale = 1,
    append = "\u2014"
  ),
  size = list(
    borders = list(
      contours = 0.15,
      water = 0.4,
      canal = 0.5,
      river = 0.6
    ),
    streets = list(
      path = 0.2,
      residential = 0.3,
      structure = 0.35,
      tertiary = 0.4,
      secondary = 0.5,
      primary = 0.6,
      motorway = 0.8,
      rails = 0.65,
      runway = 3
    )
  )
)
cityview(name = "Rio de Janeiro", zoom = 0.5, theme = myTheme, border = "square", filename = "Rio.png")

You can store the custom theme in the package cache for retrieval in a future R session with the city_themes() function. This is illustrated below for the myTheme list.

# Store the theme in the persistent cache
city_themes(name = "blackyellow", theme = myTheme)
# Retreive the theme from the persistent cache (e.g., in a future R session)
city_themes(name = "blackyellow")
# Remove the theme from the persistent cache
city_themes(name = "blackyellow", remove = TRUE)

To use a custom font in myTheme[["font"]][["family"]], simply donwload a .ttf file of the font from the web, save it as path/to/font/<font_name>.ttf and register the font via the code below. Then, use <font_name> for family.

sysfonts::font_add("<font_name>", "path/to/font/<font_name>.ttf")

Enclosing the map

There are several types of borders that can be used to enclose the city. The image above is created using border = "square", but other options for the border argument include none (the default), circle (left), rhombus (middle), square, hexagon, octagon, decagon and bbox (right).

Other display options

There are three other arguments to the cityview() function that can be used to tailor the image to your liking. First, the argument halftone allows you to add a colored dotted dither to the image (e.g., halftone = "#ffffff", left). Second, setting legend = TRUE adds a distance measurer and a compass to the image (middle). Third, the argument places takes an integer and adds that amount of names of towns, villages, suburbs, quarters and neighbourhoods to the image (e.g., places = 10, right).

