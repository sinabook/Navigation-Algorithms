from Address import get_address
import timeit 

def ids_with_backtracking(matrix, start, goal, max_depth):
    rows, cols = len(matrix), len(matrix[0])

    def dfs_recursive(current_state, depth, path):
        if current_state == goal:
            print("Path found:", path + [current_state])
            return True

        if depth == 0:
            return False

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if successor not in path:  # Avoid revisiting nodes
                if dfs_recursive(successor, depth - 1, path + [current_state]):
                    return True

        return False

    for depth in range(max_depth + 1):
        if dfs_recursive(start, depth, []):
            return True

    return False

time_taken = timeit.timeit(lambda: ids_with_backtracking(matrix,start=addresses_of_R, goal=addresses_of_T), number=1)
result = ids_with_backtracking(matrix_example, start_position, goal_position, max_depth=5)
if result:
    print("We have reached the answer.")
    print (f"Execution time: {time_taken} seconds")
else:
    print("We have not reached the answer.")
