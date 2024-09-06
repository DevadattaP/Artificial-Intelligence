def dfs_water_jug(jug1_capacity, jug2_capacity, target_amount, current_state, path, visited):
    if target_amount in current_state:
        return path

    visited.add(current_state)

    # Try all possible actions: fill jug1, fill jug2, pour from jug1 to jug2, pour from jug2 to jug1
    actions = [
        (jug1_capacity, current_state[1]),
        (current_state[0], jug2_capacity),
        (0, current_state[1]),
        (current_state[0], 0),
        (min(jug1_capacity, current_state[0] + current_state[1]), max(0, current_state[0] + current_state[1] - jug1_capacity)),
        (max(0, current_state[0] + current_state[1] - jug2_capacity), min(jug2_capacity, current_state[0] + current_state[1]))
    ]

    for action in actions:
        if action not in visited:
            new_path = list(path)
            new_path.append(action)
            result = dfs_water_jug(jug1_capacity, jug2_capacity, target_amount, action, new_path, visited)
            if result:
                return result

    return None


# Function to print the solution path
def print_solution_path(solution_path):
    for idx, state in enumerate(solution_path):
        print(f"Step {idx}: Jug 1: {state[0]} liters, Jug 2: {state[1]} liters")


# Example usage:
jug1_capacity = 4   # 4,5,11
jug2_capacity = 3   # 3,3,4
target_amount = 2   # 2,2,1
initial_state = (0, 0)

solution_path = dfs_water_jug(jug1_capacity, jug2_capacity, target_amount, initial_state, [initial_state], set())
if solution_path:
    print("Solution Path:")
    print_solution_path(solution_path)
else:
    print(f"Target amount {target_amount} cannot be achieved with the given jug capacities.")
