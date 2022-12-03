lines = []
with open('day3.txt') as f:
    while line := f.readline():
        lines.append(line)
solutions = []
for index, line in enumerate(lines):
    lines[index] = lines[index][:-1]
    first_half  = line[:len(line)//2]
    second_half = line[len(line)//2:]
    solutions.append(set(first_half).intersection(set(second_half)).pop())
    
print(sum(list(map(lambda x: ord(x) - 96 if x.islower() else ord(x)-38, solutions))))
