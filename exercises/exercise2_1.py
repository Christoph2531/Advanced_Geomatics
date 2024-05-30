from pyqgis_scripting_ext.core import *
canvas = HMapCanvas.new()

longitudes=[]
for i in range(-180,180,6):
    longitudes.append([[i,0],[i,180]])

for line in longitudes:
    canvas.add_geometry(HLineString.fromCoords(line),"red",2)

#osm=HMap.get_osm_layer()
#canvas.set_layers([osm])

canvas.add_geometry(HPolygon.fromCoords([[0, 0], [0, 180], [360,180], [360, 0], [0, 0]]),"red",2)

canvas.set_extent([0, 0, 360, 180])
canvas.show()