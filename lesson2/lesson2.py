myList=["Merano", "Bolzano","Trento"]

print("The elements start at position 0: ",myList[0])
myList.append("Postdam")
print(myList)
myList.remove("Postdam")
print(myList)
myList.pop(0)
print(myList)
doIhaveBolano="Bolzano" in myList
print(doIhaveBolano)
doIhavePotsdam="Bolzano" in myList
print(doIhavePotsdam)

for item in myList:
    print(item)
    
colors=["red", "green", "blue", "purple"]
ratios=[0.2,0.3,0.1,0.4]

for index in range(len(colors)):
    color=colors[index]
    ratio=ratios[index]
    
    print(f"{color} -> {ratio}")
    
for i in range(10):
    if i ==5:
        break
    print(f"A) {i}")
print("---------")    
for i in range(10):
    if i ==5:
        continue
    print(f"B) {i}")
print("---------")

for i in range(0,10,2):
    print(f"C){i}")
    
for i in range(10,0,-2):
    print(f"D) {i}")

myList.sort()
print(f"My sorted list: {myList}")
myList.sort(reverse=True)

myList=["banana","Orange","Kiwi","cherry"]
myList.sort()
print(myList)
myList.sort(key=str.lower)
print(myList)

numList=["002","01","3","004"]

def toInt(string):
    return int(string)
numList.sort(key=toInt)
print(numList)
list=[1.0,2.0,3.5,6,11,34,12]

s=0
count=0
for i in list:
    s+=i
    count+=1
avg=s/count
print(avg)
v=0
for i in list:
    v+=((i-avg)**2/(len(list)-1))
print(v)

#dictionaries
townsProvincesMap={"merano":"BZ","bolzano":"BZ","trenot":"IN"}
print(townsProvincesMap)
print(townsProvincesMap["merano"])
townsProvincesMap["potsdam"]="BR"
print(townsProvincesMap)
townsProvincesMap.pop("potsdam")
print(townsProvincesMap)

# if townsProvincesMap.get("merano") is None:
#     print("key doesn't exist"
# else:
#     print("key exists")
    
for key, value in townsProvincesMap.items():
    print(key,"is the province of", value)

filePath="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson2/data.txt"
data="""# stationid,datatime,temperature
1,2023-01-01 00:00, 12.3
2,2023-01-01 00:00, 11.3
3,2023-01-01 00:00, 10.3
"""

with open(filePath, "w") as file:
    file.write(data)
    
with open(filePath, "a") as file:
    file.write("\n1, 2023-01-02 00:00, 9.3")
    file.write("\n2, 2023-01-02 00:00, 8.3")
    
with open(filePath, "r") as file:
    lines=file.readlines()
    
print(lines)

stationsCount={}
for line in lines:
    line=line.strip()
    if line.startswith("#") or len(line)==0:
        continue
    lineSplit=line.split(",")
    stationId=lineSplit[0]
    
    counter=stationsCount.get(stationId,0)
    counter+=1
    stationsCount[stationId]=counter
    print(stationsCount)