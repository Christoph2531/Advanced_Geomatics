#9
print("exercise 9:")
data="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/01_exe9_data.csv"
with open(data, "r") as file:
    for line in file:
        if line.strip():
            if line.startswith("#") or len(line)==0:
                continue
            print(line.strip())
            
#10
print("exercise 10:")
with open(data, "r") as file:
    for line in file:
        if line.strip():
            if line.startswith("#") or len(line)==0:
                continue
            lineSplit=line.split(',')
            value=lineSplit[1]
            if 0<=float(value)<=1000:
                print(line.strip())
                
#11
print("exercise 11:")
data="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/01_exe11_data.csv"

with open(data, "r") as file:
    for line in file:
        if line.strip():
            lineSplit=line.split(';')
            for s in lineSplit:
                key, value = s.strip().split('=')
                if key.lower() == 'base':
                    base = float(value.replace('cm', ''))
                elif key.lower() == 'height':
                    height = float(value)
            print(f"base * height / 2 = {base} * {height*100} = {base*height*100/2}cm2")
            
#12/1
print("exercise 12/1:")
who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44
} 
what ={
44: "runs",
11: "dreams",
201: "plays",
23: "walks"
} 
where ={
44: "to town.",
11: "in her bed.",
201: "in the livingroom.",
23: "up the mountain."
}

for name, Id in who.items():
    action = what.get(Id)
    place = where.get(Id)
    print(f"{name} {action} {place}")
    
#12/2
who = {
"Daisy": 11,
"Joe": 201,
"Will": 23,
"Hanna": 44
} 
what ={
44: "runs",
11: "dreams",
201: "plays",
23: "walks"
} 
where ={
"runs": "to town.",
"dreams": "in her bed.",
"plays": "in the livingroom.",
"walks": "up the mountain."
}
for name, Id in who.items():
    action = what.get(Id)
    place = where.get(action)
    print(f"{name} {action} {place}")
    
#13
list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

list=list1+list2+list3+list4
count_a=list.count("a")
count_b=list.count("b")
count_c=list.count("c")
count_d=list.count("d")
count_e=list.count("e")
count_f=list.count("f")
count_g=list.count("g")
count_h=list.count("h")
print(f"count of a = {count_a}")
print(f"count of b = {count_b}")
print(f"count of c = {count_c}")
print(f"count of d = {count_d}")
print(f"count of e = {count_e}")
print(f"count of f = {count_f}")
print(f"count of g = {count_g}")
print(f"count of h = {count_h}")

#14
data="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/stations.txt"
with open(data, 'r') as file:
    i=0
    for line in file:
        print(line.strip())
        i+=1
        if i == 20:
            break
    
#15
with open(data, 'r') as file:
    lines=file.readlines()
i=0
for line in lines:
    if line.strip():
        if line.startswith("#") or len(line)==0:
            continue
        i+=1

print(f"count of stations = {i}")

#16
with open(data, 'r') as file:
    line=file.readline()
    lineStrip=line.strip()
    columns = lineStrip.split(',')
    num_columns = len(columns)

print(f"count of columns = {num_columns}")

#17
with open(data, 'r') as file:
    i = 0
    for line in file:
        lineStrip=line.strip()
        columns = lineStrip.split(',')
        print(','.join(columns[:2]))
        i += 1
        if i == 20:
            break

#18
with open(data, 'r') as file:
    total = 0
    count = 0
    for line in file:
        columns = line.strip().split(",")  # Assuming columns are separated by space, change to split(',') if separated by comma
        if line.startswith("#") or len(line)==0:
            continue
        value = float(columns[5])  # Extract the sixth column (index 5) and convert it to float
        total += value
        count += 1
    average = total / count
    print("average height:", average)
    
#19
with open(data, 'r') as file:
    count = 0
    total= 0
    first_line=file.readline().lstrip("#")
    first_line_split=first_line.strip().split(",")
    first_data_lines = []
    for line in file:
        if line.strip():
            if line.startswith("#") or len(line)==0:
                continue
            lineStrip=line.strip()
            columns = lineStrip.split(',')
            value=float(columns[5])
            total+=value
            count+=1
    average=total/count

print(f"File info: stations.txt")
print("-----------------------")
print(f"Stations count: {count}")
print(f"Average value: {round(average)}")
print("Available fields:")
for field in first_line_split:
    print(f"-> {field.strip()}")
print("First data lines:")
with open(data, 'r') as file:
    i=0
    for line in file:
        print(line.strip())
        i+=1
        if i == 5:
            break
         
#20
data="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/station_data.txt"
with open(data, 'r') as file:
    count = 0
    count_av=0
    total= 0
    first_line=file.readline().lstrip("#")
    first_line_split=first_line.strip().split(",")
    first_data_lines = []
    for line in file:
        if line.strip():
            if line.startswith("#") or len(line)==0:
                continue
            lineStrip=line.strip()
            columns = lineStrip.split(',')
            count+=1
            if float(columns[3])<0:
                continue
            value=float(columns[3])
            total+=value
            count_av+=1
    average=total/count_av

print(f"File info: station_data.txt")
print("-----------------------")
print(f"Stations count: {count}")
print(f"Average value: {round(average)}")
print("Available fields:")
for field in first_line_split:
    print(f"-> {field.strip()}")
print("First data lines:")
with open(data, 'r') as file:
    i=0
    for line in file:
        print(line.strip())
        i+=1
        if i == 5:
            break

#21
n=10
m=5

for i in range(n):
    print('*' * m)

#22
n=10

for i in range(1, n + 1):
    print('*' * i)
    
#23
n=10

for i in range(n, 0, -1):
    print('*' * i)
    
#24
a=10

even_numbers=[i for i in range(0, a + 1) if i % 2 == 0]
print("even numbers from 0 to", a, ":", even_numbers)
sum_even_numbers=sum(even_numbers)
print("sum of even numbers:", sum_even_numbers)

#25
numbers=[123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
even_numbers=[i for i in numbers if i % 2 == 0]
print("even numbers from 0 to", a, ":", even_numbers)
sum_even_numbers=sum(even_numbers)
print("sum of even numbers:", sum_even_numbers)

#26
data1="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/01_exe26_dataset1.csv"
data2="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/01_exe26_dataset2.csv"
def text_to_dict(filename):
    data_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#id'):
                fields = line.strip().split(",")
                key = fields[0]
                data_dict[key] = fields[1:]
    return data_dict

dataset1_dict = text_to_dict(data1)
dataset2_dict = text_to_dict(data2)

merged_dict = {}
for key in dataset1_dict.keys() & dataset2_dict.keys():
    merged_dict[key] = dataset1_dict[key] + dataset2_dict[key]

sorted_merged_dict = dict(sorted(merged_dict.items(), key=lambda item: int(item[0])))

for key, value in sorted_merged_dict.items():
    print(key, value)