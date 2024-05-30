from pyqgis_scripting_ext.core import *

#cleanup
#HMap.remove_layers_by_name(["OpenStreetMap",citiesName, countriesName,"test"])

folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson6/packages/"
folder_lesson7="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson7/"

geopackagePath=folder+"natural_earth_vector.gpkg"
countriesName="ne_50m_admin_0_countries"
citiesName="ne_50m_populated_places"
riversName="ne_10m_rivers_lake_centerlines_scale_rank"


#load openstreetmap files layer
osm=HMap.get_osm_layer()
HMap.add_layer(osm)

#load countries layer
citiesLayer=HVectorLayer.open(geopackagePath, citiesName)
countriesLayer=HVectorLayer.open(geopackagePath, countriesName)

citiesLayer.subset_filter("SOV0NAME='Italy'")
pointStyle=HMarker("square",4,45)+\
                HFill("0,green,0,128")+HStroke("black",1)
                
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

#lines layer
riversLayer=HVectorLayer.open(geopackagePath,riversName)
riversLayerItaly=riversLayer.sub_layer(italyGeometry,"rivers_italy",["scalerank","name"])

#thematic styling
ranges=[
    [0,0],
    [1,5],
    [6,7],
    [8,9],
    [10,11]
]
styles=[
    HStroke("blue",7),
    HStroke("blue",5),
    HStroke("blue",3),
    HStroke("blue",2),
    HStroke("blue",1)]


#riversStyle=HStroke("blue",2)
labelProperties={
    "font":"Arial",
    "color":"black",
    "size":10,
    "field":"name",
    "along_line":True,
    "bold":True,
    "italic":True
}
labelStyle=HLabel(**labelProperties)+HHalo("white",1)
#riversStyle+=labelStyle
riversLayerItaly.set_graduated_style("scalerank",ranges,styles,labelStyle)
#riversLayerItaly.set_style(riversStyle)

citiesLayer.set_style(pointStyle)
HMap.add_layer(countriesLayer)
HMap.add_layer(citiesLayer)
HMap.add_layer(riversLayerItaly)

crs=countriesLayer.prjcode

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
        
expressions="Name like 'I%' AND POP_EST>30000000"
filteredCountriesFeatures=countriesLayer.features(expressions)
count=0
for feature in filteredCountriesFeatures:
    print(feature.attributes[nameIndex])
    count+=1
print("Feature count wih filter", count)

lon=11.119982
lat=46.080428

point=HPoint(lon,lat)
buffer=point.buffer(2)
citiesLayer=HVectorLayer.open(geopackagePath,citiesName)
#HMap.add_layer(citiesLayer)

citiesNameIndex=citiesLayer.field_index("NAME")
aoi=buffer.bbox()

count=0
for feature in citiesLayer.features(bbox=aoi):
    print(feature.attributes[citiesNameIndex])
    count+=1
print("Cities features listed:",count)

#create data
#create a schema
fields={
    "id":"Integer",
    "name":"String"
}
just2citiesLayer=HVectorLayer.new("test","Point","EPSG:4326", fields)
just2citiesLayer.add_feature(HPoint(-122.42,37,78),[1,"San Francisco"])
just2citiesLayer.add_feature(HPoint(-122.42,37,78),[1,"San Francisco"])
just2citiesLayer.add_feature(HPoint(-73.98,40.47),[2,"New York"])

path=folder_lesson7+"test.gpkg"
error=just2citiesLayer.dump_to_gpkg(path,overwrite=True)
if error: 
    print(error)
HMap.add_layer(just2citiesLayer)

testLayer=HVectorLayer.open(path,"test")
HMap.add_layer(testLayer)


fields={
    "id":"Integer",
    "name":"String",
    "lat":"Double",
    "lon":"Double"
}
oneCityMoreAttributes=HVectorLayer.new("test2","Point","EPSG:4326",fields)
oneCityMoreAttributes.add_feature(HPoint(-73.98,40.47),\
["New York", 19040000,40.47,-73.98])

hopeNotError=oneCityMoreAttributes.dump_to_gpkg(path, overwrite=False)
if hopeNotError:
    print(hopeNotError)
HMap.add_layer(testLayer)

