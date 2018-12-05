data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())

twosum = 0
threesum = 0
for word in data:
    letters = {}
    for c in word:
        if c not in letters:
            letters[c] = 1
        else:
            if letters[c] == 1:
                letters[c] = 2
            elif letters[c] == 2:
                letters[c] = 3
            else:
                letters[c] = 99

    values = letters.values()
    if 2 in values:
        twosum += 1
    if 3 in values:
        threesum += 1

print(f"Solution={twosum*threesum}")
