from Address import get_address

def ids_with_backtracking(matrix, start,max_depth):
    visited = set()

    counter=0
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)

    def dfs_recursive(current_state, depth, path):
        if "T" in matrix[current_state[0]][current_state[1]] and counter == count_of_T:
            return True
        if "T" in matrix[current_state[0]][current_state[1]] and counter != count_of_T:
            counter += 1
        visited.add(current_state)

        if depth == 0:
            return False

        x, y = current_state
        addresses = get_address(matrix, x, y, visited=visited)

        for address in addresses:
            if address not in path:
                if dfs_recursive(address, depth - 1, path + [current_state]):
                    return True
        visited.remove(current_state)  

        return False

    for depth in range(max_depth + 1):
        if dfs_recursive(start, depth, []):
            return [True,visited]

    return [False,visited]


