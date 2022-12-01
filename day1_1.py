lines = []
with open('day1_1.txt') as f:
    while line := f.readline():
        lines.append(line)
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    
max_cal = 0
current_cal = 0
for calories in lines:
    if calories == "":
        max_cal = max(max_cal, current_cal)
        current_cal = 0
    else: 
        current_cal += int(calories)
print(max_cal)