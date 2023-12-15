from queue import Queue

def bfs(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])

    visited = set()
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        current_state = queue.get()

        if current_state == goal:
            return True  # هدف پیدا شده است

        x, y = current_state
        successors = get_successors(matrix, x, y)

        for successor in successors:
            if successor not in visited:
                queue.put(successor)
                visited.add(successor)

    return False  # هدف پیدا نشده است



result = bfs(matrix_example, start_position, goal_position)
if result:
    print()
else:
    print()
