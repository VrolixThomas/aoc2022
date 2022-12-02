lines = []
with open('day2.txt') as f:
    while line := f.readline():
        lines.append(line)
for i in range(len(lines)):
    lines[i] = lines[i][:-1].split(" ")
    


def calculate_round(round):
    scores = {'X': 1, "Y": 2, "Z":3}
    options = ["X", "Y", "Z"]
    convert = {"A": "X", "B":"Y", "C":"Z"}
    if convert.get(round[0]) == round[1]:
        return 3 + scores[round[1]]
    elif options[scores[convert[round[0]]]-1] == options[scores[round[1]]-2]:
        return 6 + scores[round[1]]
    else:
        return scores[round[1]]
        
score = sum(list(map(calculate_round, lines)))
print(score)
    