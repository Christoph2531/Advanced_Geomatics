from pyqgis_scripting_ext.core import *


folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/packages/"

geopackagePath=folder+"natural_earth_vector.gpkg"
citiesName="ne_50m_populated_places"
countriesName="ne_50m_admin_0_countries"


#load countries layer
citiesLayer=HVectorLayer.open(geopackagePath, citiesName)
countriesLayer=HVectorLayer.open(geopackagePath, countriesName)
    
crs=citiesLayer.prjcode
#print("Projection",crs)
#print("Spatial extent:", citiesLayer.bbox())
#print("Feature count:", citiesLayer.size())

#print("Attributes for France:")
country_nameIndex=countriesLayer.field_index("NAME")

countriesFeatures=countriesLayer.features()
for country_feature in countriesFeatures:
    country_name=country_feature.attributes[country_nameIndex]
    if country_name=="France":
        print("found it")
        country_polygon=country_feature.geometry
        #print("Geom:", country_polygon.asWkt()[:50]+"...")


#country_nameIndex=citiesLayer.field_index("ADM0NAME")
city_nameIndex=citiesLayer.field_index("NAME")

citiesFeatures=citiesLayer.features()
print("Cities of France:")
for feature in citiesFeatures:
    city_name=feature.attributes[city_nameIndex]
    cities_geometry=feature.geometry
    if cities_geometry.intersects(country_polygon):
        print(city_name)



        
