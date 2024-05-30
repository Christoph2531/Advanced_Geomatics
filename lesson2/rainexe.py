filePath="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson2/01_exe_rain_data_1year.txt"

with open(filePath, "r") as file:
    lines=file.readlines()

date2values={}

for l in lines[0:5]:
    l=l.strip()
    if l.startswith("#") or len(l)==0:
        continue
    #print(l)
    lineSplit=l.split(",")
    date=lineSplit[0]
    value=float(lineSplit[1])
    print(date,":",value)
    
    month=date[:-2]
    print(month,":",value)
    
    
    values=date2values.get(month,[])
    values.append(value)
    date2values[month]=values
    
    print(date2values)
    
for month, values in date2values.items():
    #print(month, values)
    cumRain=sum(values)
    print(f"cumulated rain for month {month} is {cumRain}")