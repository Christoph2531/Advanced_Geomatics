from pyqgis_scripting_ext.core import *

folder_natural_earth="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson6/packages/"


geopackagePath=folder+"natural_earth_vector.gpkg"
countriesName="ne_50m_admin_0_countries"

HMap.remove_layers_by_name(["OpenStreetMap"])
osm=HMap.get_osm_layer()
HMap.add_layer(osm)

#load countries layer
countriesLayer=HVectorLayer.open(geopackagePath, countriesName)

crs=countriesLayer.prjcode

field="NAME"
#pointStyle+=HLabel(field,yoffset=-8)+HHalo("white",1)
field="if(POP_MAX>100000, concat(NAME, ' (',round(POP_MAX/100000,1),')'),NAME)"

labelProperties={
    "font":"Arial",
    "color":"black",
    "size":10,
    "field":field,
    "xoffset":0,
    "yoffset":-8
}
pointStyle+=HLabel(**labelProperties)+HHalo("white",1)

#polygons layer
countriesLayer=HVectorLayer.open(geopackagePath, countriesName)
countriesLayer.subset_filter("NAME='Italy'")
italyGeometry=countriesLayer.features()[0].geometry

print(italyGeometry.centroid())

polygonStyle=HFill("0,255,0,128")
countriesLayer.set_style(polygonStyle)