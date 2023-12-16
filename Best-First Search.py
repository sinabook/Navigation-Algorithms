from queue import PriorityQueue

def best_first_search(matrix, start, goals):
    rows, cols = len(matrix), len(matrix[0])

    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        _, current_state = priority_queue.get()

        if current_state in goals:
            return True 

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if successor not in visited:
                priority = Heuristic(matrix, successor, goals)
                priority_queue.put((priority, successor))
                visited.add(successor)

    return False  


start_position = (0, 0) 
goal_positions = [(5, 5), (2, 2)] 

result = best_first_search(matrix_example, start_position, goal_positions)
if result:
    print()
else:
    print()
