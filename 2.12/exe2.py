def find_correct_value(data):
    for i in range(len(data[0])):
        new_data = {}
        for word in data:
            new_word = word[:i] + word[i+1:]
            if new_word in new_data:
                print(f"Found the duplicate word: {new_word}")
                return 0
            new_data[new_word] = 1

data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())

find_correct_value(data)
