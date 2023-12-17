import heapq
import timeit 

def ucs_with_backtracking(matrix, start, goal):
    visited = set()       
    visited_nodes = []    
    priority_queue = [(0, start)]  

    while priority_queue:
        cost, current_state = heapq.heappop(priority_queue)

        if current_state == goal:
            visited_nodes.append(current_state)
            print("Path found:", visited_nodes)
            return True  

        visited.add(current_state)
        visited_nodes.append(current_state)

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if successor not in visited:
                new_cost = cost + 1  
                heapq.heappush(priority_queue, (new_cost, successor))
                visited.add(successor)

    print("Goal not found.")
    return False

# Example usage:
result = ucs_with_backtracking(matrix_example, start_position, goal_position)
time_taken = timeit.timeit(lambda: ucs_with_backtracking(matrix_example, start_position, goal_position), number=1)
print (f"Execution time: {time_taken} seconds")

if result:
    print()
else:
    print()
