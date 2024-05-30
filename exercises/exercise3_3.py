from pyqgis_scripting_ext.core import *

folder_natural_earth="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/packages/"


geopackagePath=folder+"natural_earth_vector.gpkg"
countriesName="ne_50m_admin_0_countries"

HMap.remove_layers_by_name(["OpenStreetMap"])
osm=HMap.get_osm_layer()
HMap.add_layer(osm)

#load countries layer
countriesLayer=HVectorLayer.open(geopackagePath, countriesName)

crs=countriesLayer.prjcode

fields={
    "id":"Integer",
    "name":"String"
}
centroidsLayer=HVectorLayer.new("centroids","Point","EPSG:4326", fields)
nameIndex=countriesLayer.field_index("NAME")
#print(nameIndex)
countriesFeatures=countriesLayer.features()
for feature in countriesFeatures:
    name=feature.attributes[nameIndex]
    country_geometry=feature.geometry
    centroid=country_geometry.centroid()
    centroidsLayer.add_feature(centroid,[nameIndex,name])
    if not country_geometry.contains(centroid):
        print(name)
    
HMap.add_layer(centroidsLayer)

