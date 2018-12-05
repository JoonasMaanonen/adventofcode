def check_fabric(fabric, x, y, dimx, dimy):
    for j in range(y, y+dimy):
        for i in range(x, x+dimx):
            if fabric[i][j] == 0:
                fabric[i][j] = 1
            else:
                fabric[i][j] = 'x'
    return 0


def check_id_not_overlapping(fabric, x, y, dimx, dimy, id):
    for j in range(y, y+dimy):
        for i in range(x, x+dimx):
            if fabric[i][j] == 'x':
                return 1
    return 0



data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())

n = 1000
m = 1000
fabric = [[0] * m for i in range(n)]

for value in data:
    splitted = value.split()
    id = splitted[0]
    x, y = splitted[2].strip(":").split(",")
    dimx, dimy = splitted[3].split("x")
    x, y, dimx, dimy = int(x), int(y), int(dimx), int(dimy)
    check_fabric(fabric, x, y, dimx, dimy)

for value in data:
    splitted = value.split()
    id = splitted[0]
    x, y = splitted[2].strip(":").split(",")
    dimx, dimy = splitted[3].split("x")
    x, y, dimx, dimy = int(x), int(y), int(dimx), int(dimy)
    rvalue = check_id_not_overlapping(fabric, x, y, dimx, dimy, id)
    if rvalue == 0:
        print(f"Found non overlapping ID={id}")





sum = 0
for j in range(n):
    for i in range(m):
        if fabric[i][j] == 'x':
            sum += 1

print(f"Solution: {sum}")

