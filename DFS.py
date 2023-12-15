def dfs(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])

    visited = set()

    def dfs_recursive(current_state):
        if current_state == goal:
            return True   

        visited.add(current_state)

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if successor not in visited:
                if dfs_recursive(successor):
                    return True

        return False

    return dfs_recursive(start)

result = dfs(matrix_example, start_position, goal_position)
if result:
    print()
else:
    print()
