from pyqgis_scripting_ext.core import *

point=HPoint(30.0,10.0)
print(point.asWkt())

coords= [[31,11],[10,30],[20,40],[40,40]]
line=HLineString.fromCoords(coords)
print(line)

coords=[[32,12],[10,20],[20,39],[40,39],[32,12]]
polygon=HPolygon.fromCoords(coords)
print(polygon)

exteriorPoints=[[35,10],[10,20],[15,40],[45,45],[35,10]]
holePoints=[[20,30],[35,35],[30,20],[20,30]]
PolygoneWithHole=HPolygon.fromCoords(exteriorPoints)

HoleRing=HLineString.fromCoords(holePoints)
PolygoneWithHole.add_interior_ring(HoleRing)

multipoints=HMultiPoint.fromCoords(coords)

print(PolygoneWithHole)

coords1 = [[30,20], [10,40], [45,40], [30,20]]
coords2 = [[15,5], [40,10], [10,20], [5,10], [15,5]]
multiPolygon = HMultiPolygon.fromCoords([coords1, coords2])

coords1 = [[10,10],[20,20],[10,40]]
coords2 = [[40,40],[30,30],[40,20],[30,10]]
multiLine = HMultiLineString.fromCoords([coords1, coords2])
20

coordinates=polygon.coordinates()
for coord in coordinates:
    print(f"coord x ={coord[0]}/coord y ={coord[1]}")
    
    
wkt = "POINT (156 404)"
pointGeom = HGeometry.fromWkt(wkt)

wkt = """
MULTIPOLYGON (((130 510, 140 450, 200 480, 210 570, 150 630, 130 560, 130 510)),
((430 770, 370 820, 210 860, 20 760, 35 631, 100 370, 108 363, 154 284, 230 380,
140 400, 150 440, 130 450, 104 585, 410 670, 440 590, 450 590, 430 770)))
"""
polygonGeom = HGeometry.fromWkt(wkt)
canvas=HMapCanvas.new()
canvas.add_geometry(polygonGeom,"blue",2)

subGeometries = multiPolygon.geometries()
colorsList=["red","blue","green"]

# canvas=HMapCanvas.new()
# for i in range(len(subGeometries)):
#     geom=subGeometries[i]
#     col=colorsList[i]
#     canvas.add_geometry(geom,col,2)

# canvas=HMapCanvas.new()
# canvas.add_geometry(multiPolygon,"blue",2)
# canvas.add_geometry(multiLine,"blue",2)
# canvas.set_extent([0,0,50,50])
canvas.set_extent([0,0,50,50])
canvas.show()

# canvas=HMapCanvas.new()
# canvas.add_geometry(point,"red",2)
# canvas.add_geometry(line,"black",2)
# canvas.add_geometry(polygon,"green",2)
# canvas.add_geometry(PolygoneWithHole,"blue",2)
# canvas.set_extent([0,0,50,50])
# canvas.show()

#Homework UTM grid 6 degrees
#also create a test set"no labels