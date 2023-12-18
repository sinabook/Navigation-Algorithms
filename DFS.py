from Address import get_address
def dfs_with_backtracking(matrix, start):
    visited = set()
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    counter = 0
    def dfs_recursive(current_state, counter, count_of_T):
        if "T" in matrix[current_state[0]][current_state[1]] and counter == count_of_T:
            return [True,visited]
        if "T" in matrix[current_state[0]][current_state[1]] and counter != count_of_T:
            counter += 1
        visited.add(current_state)
        x = current_state[0]
        y = current_state[1]
        addresses = get_address(matrix, x, y, visited=visited)

        for address in addresses:
            if address not in visited:
                if dfs_recursive(address, counter, count_of_T):
                    return [True,visited]

        visited.remove(current_state)  
        return [False,visited]
    list=dfs_recursive(start, counter=counter, count_of_T=count_of_T)
    return list


