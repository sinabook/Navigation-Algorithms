from queue import Queue
from Address import get_address
def bfs(matrix, start, goal):
    start=start[0]
    rows, cols = len(matrix), len(matrix[0])
    x=start[0]
    y=start[1]
    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)
    counter=0
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)

    while not queue.empty():
        current_state = queue.get()
        if "T" in matrix[current_state[0]][current_state[1]] and counter==count_of_T:
            return True  # هدف پیدا شده است
        if current_state in goal and counter!=count_of_T:
            counter+=1
        x=current_state[0]
        y=current_state[1]
        addresses = get_address(matrix, x, y,visited=visited)

        for address in addresses:
            if address not in visited:
                queue.put(address)
                visited.add(address)
    print(visited)
    return False  # هدف پیدا نشده است



matrix=[["1R","1","1","5","5","4","2C","1","15","1B"],
        ["1","1","5","3","5","5","4","5","X","X"],
        ["5","1I","1","6","2","2","2","1","1","1T"],
        ["X","X","1","6","5","5","2","1","1","X"],
        ["X","X","1","X","X","50","2","1C","1","X"],
        ["1","1","1","2","2","2T","2","1","1","1"]
        ]
addresses_of_R = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'R' in cell]
addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]

result = bfs(matrix,start=addresses_of_R,goal=addresses_of_T)
if result:
    print("We have reached all answers")
    print(result)
else:
    print("We have not reached all answers")
    print(result)