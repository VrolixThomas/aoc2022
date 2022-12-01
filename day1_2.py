lines = []
with open('day1_1.txt') as f:
    while line := f.readline():
        lines.append(line)
for i in range(len(lines)):
    lines[i] = lines[i][:-1]

all_calories = []
current_cal = 0
for calories in lines:
    if calories == "":
        all_calories.append(current_cal)
        current_cal = 0
    else: 
        current_cal += int(calories)
all_calories = sorted(all_calories, reverse=True)
print(sum(all_calories[:3]))