from  collections import defaultdict
import string

WORKERS = 5

def removeElement(keys, tree):
    prereqs = []
    for key, value in tree.items():
        for letter in value:
            prereqs.append(letter)

    possible_executables = []
    for key in keys:
        if key not in prereqs:
            possible_executables.append(key)

    possible_executables.sort()
    return possible_executables[0]

def getPossibleExecutables(keys, tree):
    prereqs = []
    for key, value in tree.items():
        for letter in value:
            prereqs.append(letter)

    possible_executables = []
    for key in keys:
        if key not in prereqs:
            possible_executables.append(key)

    possible_executables.sort()
    return possible_executables

# GET data
data = []
with open("input.txt") as f:
    for line in f:
        split = line.strip().split()
        first = split[1]
        second = split[7]
        data.append((first, second))

tree = defaultdict(list)
keys = []
allvalues = []
for value in data:
    tree[value[0]].append(value[1])
    if value[0] not in keys:
        keys.append(value[0])
    if value[1] not in allvalues:
        allvalues.append(value[1])

order = ""
while tree:
    element = removeElement(keys, tree)
    if element in allvalues:
        allvalues.remove(element)
    tree.pop(element)
    keys.remove(element)
    order = order + element


order = order + allvalues[0]
print(f"PART1 Order: {order}")

order = ""

############# PART 2 ##################

durations = {}
letters = string.ascii_uppercase
for index, letter in enumerate(letters):
    durations[letter] = index + 1 + 60


queue = {}
tree = defaultdict(list)
keys = []
allvalues = []
for value in data:
    tree[value[0]].append(value[1])
    if value[0] not in keys:
        keys.append(value[0])
    if value[1] not in allvalues:
        allvalues.append(value[1])

remove = 0
for value in allvalues:
    if value not in keys:
        remove = value

time = 0
while tree:
    # Reduce all units in the queue by one
    toRemove = []
    for key, value in queue.items():
        queue[key] -= 1
        if queue[key] == 0:
            toRemove.append(key)

    for key in toRemove:
        tree.pop(key)
        queue.pop(key)
        order = order + key

    executables = getPossibleExecutables(keys, tree)
    amountToAdd = WORKERS - len(queue)
    for i in range(amountToAdd):
        if i == len(executables):
            break
        letter = executables[i]
        queue[letter] = durations[letter]
        keys.remove(letter)

    time += 1

order = order + remove
time += durations[remove] - 1
print(f"PART2: time={time}")
#print(f"order={order}")
