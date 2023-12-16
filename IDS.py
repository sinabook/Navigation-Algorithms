def ids(matrix, start, goal, max_depth):
    rows, cols = len(matrix), len(matrix[0])

    def dfs_recursive(current_state, depth):
        if current_state == goal:
            return True 

        if depth == 0:
            return False

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if dfs_recursive(successor, depth - 1):
                return True

        return False

    for depth in range(max_depth + 1):
        if dfs_recursive(start, depth):
            return True

    return False  


result = ids(matrix_example, start_position, goal_position, max_depth=5)
if result:
    print()
else:
    print()
