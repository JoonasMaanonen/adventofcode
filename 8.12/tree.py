def preprocess_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip().split())

    data = [int(char) for char in data[0]]
    return data

def traverse_tree(data):
    n_children, n_meta = data[0], data[1]
    data = data[2:]
    totals = 0
    values = []
    for i in range(n_children):
        total, value, data = traverse_tree(data)
        totals += total
        values.append(value)

    totals += sum(data[i] for i in range(n_meta))
    if n_children == 0:
        value = (sum(data[i] for i in range(n_meta)))
    else:
        meta_data = data[:n_meta]
        value = sum(values[value-1] for value in meta_data if len(values) >= value)
    return totals, value, data[n_meta:]

def main():
    data = preprocess_data("input.txt")
    total, value, remaining_data = traverse_tree(data)
    print(f"PART 1: {total}")
    print(f"PART 2: {value}")

if __name__== "__main__":
    main()
