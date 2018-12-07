import math
import operator

def manhattan_distance(coord1, coord2):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance

# Preprocessing
coordinates = []
xcoords = []
ycoords = []
with open("input.txt") as f:
    for line in f:
        coord = line.strip().split(",")
        x = int(coord[0])
        y = int(coord[1].strip())
        xcoords.append(x)
        ycoords.append(y)
        coordinates.append((x, y))


# Define our grid
m = max(ycoords) + 1
n = max(xcoords) + 1
grid = [['UD'] * m for i in range(n)]
lista = [i for i in range(len(coordinates))]

# Check part 2 here
max_distance = 10000
for y in range(m):
    for x in range(n):
        c1 = (x, y)
        total_distance = 0
        for c2 in coordinates:
            distance = manhattan_distance(c1, c2)
            total_distance += distance

        if total_distance < max_distance:
            grid[x][y] = '#'


# Check occurences of #, that is our size of region
size = 0
for y in range(m):
    for x in range(n):
        if grid[x][y] == '#':
            size += 1

print(f"PART2: Size of region={size}")
# Part 1
for y in range(m):
    for x in range(n):
        c1 = (x, y)
        closest = math.inf
        distance = math.inf
        leader = -1
        for c2 in coordinates:
            distance = manhattan_distance(c1, c2)
            if distance < closest:
                closest = distance
                leader = c2
            elif distance == closest:
                leader = 'MULTIPLE'
            else:
                pass
        # Here we know which coord is closest
        grid[x][y] = leader


areas = coordinates

# Rows
for x in range(n):
    if grid[x][0] in areas:
        areas.remove(grid[x][0])
    if grid[x][m-1] in areas:
        areas.remove(grid[x][m-1])

# Columns
for y in range(m):
    if grid[0][y] in areas:
        areas.remove(grid[0][y])
    if grid[n-1][y] in areas:
        areas.remove(grid[n-1][y])

sums = {}
for coord in areas:
   area = sum(value.count(coord) for value in grid)
   sums[coord] = area

biggest_region = max(sums.items(), key=operator.itemgetter(1))[0]
print(f"PART1: biggest_coordinates: {biggest_region} : Region size: {sums[biggest_region]}")


