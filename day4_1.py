import re

lines = []
with open('day4.txt') as f:
    while line := f.readline():
        lines.append(line)
for i in range(len(lines) ):
    lines[i] = lines[i][:-1]
    lines[i] = re.split(',|-', lines[i])
    
    
count = 0
for line in lines:
    if int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3]):
        count += 1
    elif int(line[2]) <= int(line[0]) and int(line[3]) >= int(line[1]):
        count += 1
print(count)