from queue import Queue

class BFS:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.visited = set()

    def search(self):
        queue = Queue()
        queue.put(self.initial_state)

        while not queue.empty():
            current_state = queue.get()
            if current_state not in self.visited:
                self.visited.add(current_state)

                

                for successor_state in successor(current_state):
                    queue.put(successor_state)
