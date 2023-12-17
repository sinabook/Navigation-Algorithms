from queue import PriorityQueue
from Address import get_address
from Hueristic import Heuristic
def best_first_search(matrix, start, goals):
    counter=0
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)

    visited = set()
    start=start[0]
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        _, current_state = priority_queue.get()
        if "T" in matrix[current_state[0]][current_state[1]] and counter==count_of_T:
            return True 
        if "T" in matrix[current_state[0]][current_state[1]] and counter!=count_of_T:
            counter+=1
        x, y = current_state
        addresses = get_address(matrix,x, y,visited=visited)

        for address in addresses:
            if address not in visited:
                if(Heuristic(matrix, address,goals,visited=visited)[3]):
                    priority=Heuristic(matrix, address,goals,visited=visited)[3]
                else:
                    priority=0
                priority_queue.put((priority, address))
                visited.add(address)
        
    return False  

matrix=[["1R","1","1","5","5","4","2C","1","15","1B"],
        ["1","1","5","3","5","5","4","5","X","X"],
        ["5","1I","1","6","2","2","2","1","1","1T"],
        ["X","X","1","6","5","5","2","1","1","X"],
        ["X","X","1","X","X","50","2","1C","1","X"],
        ["1","1","1","2","2","2T","2","1","1","1"]
        ]
addresses_of_R = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'R' in cell]
addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]
result = best_first_search(matrix, start=addresses_of_R, goals=addresses_of_T)
if result:
    print("We have reached the answer")
else:
    print("We have not reached the answer")
