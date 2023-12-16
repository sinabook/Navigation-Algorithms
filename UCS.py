import heapq

def ucs(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])

    visited = set()
    priority_queue = [(0, start)]
    visited.add(start)

    while priority_queue:
        cost, current_state = heapq.heappop(priority_queue)

        if current_state == goal:
            return True  

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if successor not in visited:
                new_cost = cost + 1 
                heapq.heappush(priority_queue, (new_cost, successor))
                visited.add(successor)

    return False  


result = ucs(matrix_example, start_position, goal_position)
if result:
    print()
else:
    print()
