lines = []
with open('day3.txt') as f:
    while line := f.readline():
        lines.append(line)
solutions = []
for i in range(0,len(lines),3 ):
    lines[i] = lines[i][:-1]
    solutions.append(set(lines[i]).intersection(set(lines[i+1])).intersection(lines[i+2]).pop())
print(solutions)
    
print(sum(list(map(lambda x: ord(x) - 96 if x.islower() else ord(x)-38, solutions))))
