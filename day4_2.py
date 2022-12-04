import re

lines = []
with open('day4.txt') as f:
    while line := f.readline():
        lines.append(line)
for i in range(len(lines) ):
    lines[i] = lines[i][:-1]
    lines[i] = re.split(',|-', lines[i])


count = sum(1 for line in lines if set(range(int(line[0]), int(line[1]) + 1)).intersection(set(range(int(line[2]), int(line[3]) + 1))))

print(count)