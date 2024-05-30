from pyqgis_scripting_ext.core import *

import math

canvas = HMapCanvas.new()

n=4
d=9
k=n/d
iterations=max([n,d])
maxangle=360*iterations

coordinates=[]
for angle in range(0,maxangle,1):
    r=math.cos(k*(math.radians(angle)))
    x=r*math.cos(math.radians(angle))
    y=r*math.sin(math.radians(angle))
    
    coordinates.append([x,y])

rose=HLineString.fromCoords(coordinates)
canvas.add_geometry(rose)
canvas.set_extent([-2,-2,2,2])
canvas.show()
