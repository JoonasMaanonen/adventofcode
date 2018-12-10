import time

def insert_stone(circle, current_stone, stone):
    # Handle special case
    length = len(circle)
    if stone % 23 == 0:
        movement = current_stone - 7
        # Wrap around
        if movement < 0:
            wrap_index = length + movement
            points = circle[wrap_index] + stone
            del circle[movement]
            return circle, wrap_index, points
        else:
            points = circle[movement] + stone
            del circle[movement]
            return circle, movement, points
    else:
        last_index = length - 1
        # Handle normal movement
        if current_stone == last_index:
            circle.insert(1, stone)
            return circle, 1, 0
        else:
            if (current_stone + 1) == (last_index):
                # Between 0 and end
                circle.append(stone)
                return circle, current_stone + 2, 0
            else:
                circle.insert(current_stone+2, stone)

        return circle, current_stone + 2, 0

def init_scores(n_players):
    scores = {}
    for i in range(1, n_players+1):
        scores[i] = 0
    return scores

def main():
    n_players = 468
    last_marble = 71843
    print(f"Calculating for last marble of {last_marble}")
    start = time.time()

    scores = init_scores(n_players)
    circle = [0, 1]
    current_stone = 1
    player_index = 1
    for i in range(2, last_marble+1):
        circle, current_stone, points = insert_stone(circle, current_stone, i)
        if i % 23 == 0:
            scores[player_index] += points

        player_index += 1
        if player_index > n_players:
            # Wrap around
            player_index = 1

    highest = 0
    for k, v in scores.items():
        if v > highest:
            highest = v


    end = time.time()

    print(f"Time elapsed was {end - start}")
    print(f"PART 1: High score is {highest}")


if __name__== "__main__":
    main()
