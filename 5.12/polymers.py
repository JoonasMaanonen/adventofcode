import string

def reaction(polymer_string):
    last_unit = ""
    for i, c in enumerate(polymer_string):
        if (c != last_unit):
            if c.lower() == last_unit.lower():
                # Found a reaction pair
                polymer_string = polymer_string[:i-1] + polymer_string[i+1:]
                return polymer_string, "Reacted"
            else:
                last_unit = c
        else:
            last_unit = c
    return polymer_string, "No reaction"

data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())


original_polymer = data[0]
new_polymer = data[0]
results = {}

#Part 2 preprocessing
polymer_units = string.ascii_lowercase
for unit in polymer_units:
    opposite = unit.upper()
    new_polymer = original_polymer.replace(unit, "").replace(opposite, "")
    while(1):
        new_polymer, status = reaction(new_polymer)
        if status == "No reaction":
            results[unit] = len(new_polymer)
            print(f"Found a polymer for letter={unit}, it is {len(new_polymer)} long")
            break

print(results)

#print(f"The final polymer is: {new_polymer}")
#print(f"The length is : {len(new_polymer)}")

