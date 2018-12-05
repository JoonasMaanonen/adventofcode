data = []
with open("input.txt") as f:
    for line in f:
        data.append(int(line.strip()))

twice_hash = {"0" : 0}
sum = 0
while(1):
    for value in data:
        sum += value
        if sum in twice_hash:
            print(f"Number {sum} found twice in dataset!")
            break
        else:
            twice_hash[sum] = sum

    else:
        continue
    break

print(sum)
