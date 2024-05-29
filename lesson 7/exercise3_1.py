from pyqgis_scripting_ext.core import *
folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson7/"
path=f"{folder}stations.txt"

fields={
    "id":"Integer",
    "name":"String"
}
stationsLayer=HVectorLayer.new("stations","Point","EPSG:4326", fields)


with open(path, "r") as file:
    lines=file.readlines()
    for line in lines:
        if line.startswith("#") or len(line)==0:
            continue
        linesplit=line.strip().split(",")
        stationname=linesplit[1]
        stationid=linesplit[0]
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
        stationsLayer.add_feature(point,[stationid,stationname])

path=folder+"stations.gpkg"
error=stationsLayer.dump_to_gpkg(path,overwrite=True)
if error: 
    print(error)
HMap.add_layer(stationsLayer) 

