from queue import PriorityQueue
from Address import get_address
from Hueristic import Heuristic
def best_first_search(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    counter=0
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    addresses_of_T = [(row_idx, col_idx) for row_idx, row in enumerate(matrix) for col_idx, cell in enumerate(row) if 'T' in cell]
    priority=[]
    visited = []
    node=[]
    priority.append(0)
    node.append(start)
    i=0
    while i<=rows*cols:
        i+=1
        p=priority[-1]
        current_state=node[-1]
        if "T" in matrix[current_state[0]][current_state[1]] and counter==count_of_T:
            return [True,visited]
        if "T" in matrix[current_state[0]][current_state[1]] and counter!=count_of_T:
            counter+=1
        x, y = current_state
        addresses = get_address(matrix,x, y,visited=visited)

        for address in addresses:
            if address not in visited:
                if(Heuristic(matrix, address,addresses_of_T=addresses_of_T,visited=visited)[3]):
                    Priority=Heuristic(matrix, address,addresses_of_T=addresses_of_T,visited=visited)[3]
                else:
                    Priority=0
                priority.append(Priority)
                node.append(address)
                visited.append(address)
        
    return [False,visited]  


