data = []
sum = 0
with open("input.txt") as f:
    for line in f:
        data.append(int(line.strip()))
print(data)

for value in data:
    sum += value

print(sum)
