from pyqgis_scripting_ext.core import *
#0
folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson3/"
path = f"{folder}02_exe0_geometries.csv"
canvas = HMapCanvas.new()

with open(path,"r") as file:
    for line in file:
        parts = line.strip().split(';')
        shape_type = parts[0]
        
        coordinates = [tuple(map(float, coord.split(','))) for coord in parts[1].split()]
        print(coordinates)
        size=parts[2]
        if shape_type == "point":
            shape=HPoint(coordinates[0][0],coordinates[0][1])
            canvas.add_geometry(shape,"magenta",int(size))
        elif shape_type == "line":
            print(type(size))
            shape = HLineString.fromCoords(coordinates)
            canvas.add_geometry(shape,"blue",int(size))
        elif shape_type == "polygon":
            shape = HPolygon.fromCoords(coordinates)
            canvas.add_geometry(shape,"red",int(size))
            
canvas.set_extent([0, 0, 50, 50])
canvas.show()

