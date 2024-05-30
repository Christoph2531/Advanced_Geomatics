from pyqgis_scripting_ext.core import *

#cleanup
HMap.remove_layers_by_name(["OpenStreetMap"])

folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson6/packages/"

geopackagePath=folder+"natural_earth_vector.gpkg"
countriesName="ne_50m_admin_0_countries"



#load openstreetmap files layer
osm=HMap.get_osm_layer()
HMap.add_layer(osm)

#load countries layer
countriesLayer=HVectorLayer.open(geopackagePath, countriesName)

print("Schema (first 4 fields):")
counter=0
for name, type in countriesLayer.fields.items():
    counter+=1
    if counter<5:
        print("\t", name,"of type", type)
    
crs=countriesLayer.prjcode
print("Projection",crs)
print("Spatial extent:", countriesLayer.bbox())
print("Feature count:", countriesLayer.size())

print("Attributes for Italy:")
nameIndex=countriesLayer.field_index("NAME")
print(nameIndex)
countriesFeatures=countriesLayer.features()
for feature in countriesFeatures:
    name=feature.attributes[nameIndex]
    if name=="Italy":
        #print("found it")
        geometry=feature.geometry
        print("Geom:", geometry.asWkt()[:50]+"...")



#countriesFeatures=countriesLayer.features()
