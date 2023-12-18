import heapq
from Address import get_address

def ucs_with_backtracking(matrix, start, goal):
    visited = []      
    visited_nodes = []    
    priority_queue = [(0, start)]  
    count_of_T = sum(cell.count('T') for row in matrix for cell in row)
    counter=0
    while priority_queue:
        cost, current_state = heapq.heappop(priority_queue)

        if "T" in matrix[current_state[0]][current_state[1]] and counter == count_of_T:
            visited_nodes.append(current_state)
            return [True,visited]
        if "T" in matrix[current_state[0]][current_state[1]] and counter != count_of_T:
            counter += 1
        visited.append(current_state)
        visited_nodes.append(current_state)

        x, y = current_state
        addresses = get_address(matrix, x, y,visited=visited)

        for address in addresses:
            if address not in visited:
                new_cost = cost + 1  
                heapq.heappush(priority_queue, (new_cost, address))
                visited.append(address)

    return [False,visited]

