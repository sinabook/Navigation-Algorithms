from Address import get_address
import timeit
def dfs_with_backtracking(matrix, start):
    start = start[0]
    visited = set()
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    counter = 0

    def dfs_recursive(current_state, counter, count_of_T):
        if "T" in matrix[current_state[0]][current_state[1]] and counter == count_of_T:
            return True
        if "T" in matrix[current_state[0]][current_state[1]] and counter != count_of_T:
            counter += 1
        visited.add(current_state)
        x = current_state[0]
        y = current_state[1]
        addresses = get_address(matrix, x, y, visited=visited)

        for address in addresses:
            if address not in visited:
                if dfs_recursive(address, counter, count_of_T):
                    return True

        visited.remove(current_state)  
        return False

    return dfs_recursive(start, counter=counter, count_of_T=count_of_T)

matrix = [
    ["1R", "1", "1", "5", "5", "4", "2C", "1", "15", "1B"],
    ["1", "1", "5", "3", "5", "5", "4", "5", "X", "X"],
    ["5", "1I", "1", "6", "2", "2", "2", "1", "1", "1T"],
    ["X", "X", "1", "6", "5", "5", "2", "1", "1", "X"],
    ["X", "X", "1", "X", "X", "50", "2", "1C", "1", "X"],
    ["1", "1", "1", "2", "2", "2T", "2", "1", "1", "1"]
]

addresses_of_R = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'R' in cell]
addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]
time_taken = timeit.timeit(lambda: dfs_with_backtracking(matrix,start=addresses_of_R, goal=addresses_of_T), number=1)
result = dfs_with_backtracking(matrix, start=addresses_of_R)
if result:
    print("We have reached the answer.")
    print (f"Execution time: {time_taken} seconds")
else:
    print("We have not reached the answer.")
