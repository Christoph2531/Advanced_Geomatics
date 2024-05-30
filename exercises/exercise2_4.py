from pyqgis_scripting_ext.core import *
folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/Advanced Geomatics/data/"
path=f"{folder}stations.txt"

crsHelper=HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(32632)
input_point=HPoint(11.34999,46.49809)
input_radius=20
input_radius_m=input_radius*1000
input_point32632=crsHelper.transform(input_point)
buffer=input_point32632.buffer(input_radius_m)
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
        point32632=crsHelper.transform(point)
        if buffer.contains(point32632):
            dist=round(point32632.distance(input_point32632)/1000,0)
            print(f"{linesplit[1]} ({dist}km) -> {point}")
