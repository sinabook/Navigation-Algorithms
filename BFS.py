from Address import get_address
def bfs(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])
    x=start[0]
    y=start[1]
    visited = []
    queue = []
    queue.append(start)
    visited.append(start)
    counter=0
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    loop=0
    while loop<=rows*cols:
        loop+=1
        current_state = queue[-1]
        if "T" in matrix[current_state[0]][current_state[1]] and counter==count_of_T:
            return [True,visited]  # هدف پیدا شده است
        if current_state in goal and counter!=count_of_T:
            counter+=1
        x=current_state[0]
        y=current_state[1]
        addresses = get_address(matrix, x, y,visited=visited)

        for address in addresses:
            if address not in visited:
                queue.append(address)
                visited.append(address)
    return [False,visited]  # هدف پیدا نشده است


# time_taken = timeit.timeit(lambda: bfs(matrix,start=addresses_of_R, goal=addresses_of_T), number=1)
