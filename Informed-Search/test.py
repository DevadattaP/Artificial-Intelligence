from copy import deepcopy

initial_state = [
    [0,2,3],
    [1,4,6],
    [7,5,8]
]
# 0 is considered empty space
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
# Store the previously visited states to avoid infinite loops
state_history = []

# Function to find the Manhattan distance
def manhattan(current_state):
    if current_state not in state_history:
        total_distance = 0

        for i in range(3):
            for j in range(3):

                if current_state[i][j] == 0:
                    continue

                for k in range(3):
                    for l in range(3):

                        if current_state[i][j] == goal_state[k][l]:
                            abs_diff = abs(i - k) + abs(j - l)

                            total_distance += abs_diff

        return total_distance
    return 9999


def display(state):  # Displays the current state

    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile == 0:
                print(" ", end=" ")
            else:
                print(tile, end=" ")
        print()
    print()


def moves(state):  # Function to find all possible moves.
    possible_moves = [ 'Left', 'Up','Down', 'Right']

    # Finding the position of the empty space
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if j == 2: possible_moves.remove('Right')
                if j == 0: possible_moves.remove('Left')
                if i == 0: possible_moves.remove('Up')
                if i == 2: possible_moves.remove('Down')

                return possible_moves


def swap(current_state, i, j, move):
    current_i, current_j = i, j
    new_i, new_j = i, j

    if move == 'Up':
        # Swap it with the element above
        new_i = i - 1

    elif move == 'Right':
        # Swap it with the element right
        new_j = j + 1

    elif move == 'Down':
        # Swap it with the element down
        new_i = i + 1

    elif move == 'Left':
        # Swap it with the element left
        new_j = j - 1
    current_state[current_i][current_j] = current_state[new_i][new_j]
    current_state[new_i][new_j] = 0


def explore(state, move):  # Function to explore a move and return its heuristic score

    current_state = deepcopy(state)
    # Deepcopy is used to copy the list by value (recursively) instead of just copying the reference.

    for i in range(3):
        for j in range(3):
            if current_state[i][j] == 0:  # Finding the position of the empty space

                swap(current_state, i, j, move)
                return manhattan(current_state)


def execute(state, move):  # Function to execute a move passed as argument

    state_history.append(deepcopy(state))

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:  # Finding the position of the empty space
                swap(state, i, j, move)
                return


def __main__():
    print("Initial state :")
    display(initial_state)
    count = 0
    while initial_state != goal_state:

        possible_moves = moves(initial_state)
        best_move = possible_moves[0]
        smallest_score = explore(initial_state, best_move)

        for move in possible_moves:
            move_score = explore(initial_state, move)
            if move_score < smallest_score:
                smallest_score = move_score
                best_move = move

        execute(initial_state, best_move)
        count += 1
        print("Step ", count, " : ", best_move)
        display(initial_state)

    print("Goal !")

__main__()
