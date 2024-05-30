#19
data="C:/Users/christoph/Documents/UniBz/Advanced Geomatics/lesson1/stations.txt"

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
            if len(first_data_lines) < 3:
                first_data_lines.append(line)
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
for line in first_data_lines:
    print(",".join(line))