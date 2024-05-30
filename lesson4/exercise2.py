from pyqgis_scripting_ext.core import *
folder="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson4/"
path=f"{folder}stations.txt"
canvas = HMapCanvas.new()
countries=[]

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
        canvas.add_geometry(point,"red",0.5)
        countries.append(linesplit[2])

canvas.set_extent([-30, 30, 40, 80])
canvas.show()

setcountries=set(countries)
    
for setc in setcountries:
    print(f"{setc}: {countries.count(setc)}")
    

