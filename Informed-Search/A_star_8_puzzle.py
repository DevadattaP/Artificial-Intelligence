from copy import deepcopy

initial_state = [
    [3, 4, 0],
    [6, 1, 8],
    [2, 5, 7]
]

# 0 is considered empty space
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
# Store the previously visited states to avoid infinite loops
state_history = []


def manhattan(current_state):  # Function to find the Manhattan distance
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
    possible_moves = ['Down', 'Left', 'Right', 'Up']

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


def checkBest(state, possible_moves, index_min):
    new_states = []
    new_best_score = []
    j = 0
    for i, move in enumerate(possible_moves):
        new_score = []
        if i in index_min:
            new_states.append(deepcopy(state))
            execute(new_states[j],possible_moves[i])
            if new_states[j] not in state_history:
                new_possible_moves = moves(new_states[j])
                for n_move in new_possible_moves:
                    new_score.append(explore(new_states[j], n_move))
                print(new_score)
                new_min = min(new_score)
                new_best_score.append(new_min)

                j += 1
    print(new_states)
    
    new_minimum = min(new_best_score)
    new_index = [i for i, x in enumerate(new_best_score) if x == new_minimum]
    return new_index


def __main__():
    display(initial_state)
    count = 0
    while initial_state != goal_state:
        possible_moves = moves(initial_state)
        print(possible_moves)
        scores = []

        for move in possible_moves:
            scores.append(explore(initial_state, move))
        print(scores)
        min_score = min(scores)
        print(min_score)
        index_min = [i for i, x in enumerate(scores) if x == min_score]
        print(index_min)
        new_min = 0
        if len(index_min) > 1:
            new_index = checkBest(initial_state, possible_moves, index_min)
            if len(new_index) == 1:
                new_min = new_index[0]
        execute(initial_state, possible_moves[index_min[new_min]])
        # possible_moves = moves(initial_state)
        # best_move = possible_moves[0]
        # smallest_score = explore(initial_state, best_move)
        #
        # for move in possible_moves:
        #     move_score = explore(initial_state, move)
        #     if move_score < smallest_score:
        #         smallest_score = move_score
        #         best_move = move
        #
        # execute(initial_state, best_move)
        count += 1
        print(count)
        display(initial_state)


__main__()
