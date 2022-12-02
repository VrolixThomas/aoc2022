lines = []
with open('day2.txt') as f:
    while line := f.readline():
        lines.append(line)
for i in range(len(lines)):
    lines[i] = lines[i][:-1].split(" ")
    


def calculate_round(round):
    scores = {'X': 1, "Y": 2, "Z":3}
    convert = {"A": "X", "B":"Y", "C":"Z"}
    if round[1] == "X":
        return scores[convert[round[0]]] - 1 if round[0] != "A" else 3
    elif round[1] == "Y":
        return 3 + scores[convert[round[0]]]
    else:
        return 6 + (scores[convert[round[0]]] + 1 if round[0] != "C" else 1)
        
score = sum(list(map(calculate_round, lines)))
print(score)
    