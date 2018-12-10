def preprocess_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip().split())

    data = [int(char) for char in data[0]]
    return data


def traverse_tree(data):
    n_children, num_meta = data[0], data[1]
    data = data[2:]
    totals = 0
    for i in range(n_children):
        total, data = traverse_tree(data)
        totals += total

    totals += sum(data[i] for i in range(num_meta))
    return totals, data[num_meta:]


def main():
    data = preprocess_data("input.txt")
    total, remaining_data = traverse_tree(data)
    print(f"PART 1: {total}")


if __name__== "__main__":
    main()




