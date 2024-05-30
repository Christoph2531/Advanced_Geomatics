from pyqgis_scripting_ext.core import *
folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/Avanced Geomatics/data/"
path=f"{folder}stations.txt"
input_point=HPoint(11.34999,46.49809)
min_distance=float("inf")
points=[]
with open(path,"r") as file:
    for line in file:
        if line.startswith("#") or len(line)==0:
            continue
        linesplit=line.strip().split(",")
        lat=linesplit[3]
        lon=linesplit[4]
        latsplit=lat.split(":")
        latgrad=float(latsplit[0])
        latmin=float(latsplit[1])/60
        latsec=float(latsplit[2])/3600
        latitude=latgrad+latmin+latsec
        lonsplit=lon.split(":")
        longrad=float(lonsplit[0])
        lonmin=float(lonsplit[1])/60
        lonsec=float(lonsplit[2])/3600
        latitude=latgrad+latmin+latsec
        longitude=longrad+lonmin+lonsec
        point=HPoint(longitude,latitude)
        points.append(point)
        dist=input_point.distance(point)
        if dist < min_distance:
            min_distance=dist
            nearest_point=point
            nearest_location=linesplit[1]
print(f"{nearest_location} -> {nearest_point}")
        

