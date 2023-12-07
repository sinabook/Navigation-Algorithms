import heapq

class BestFirstSearch:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.visited = set()

    def heuristic(self, state):
        
        pass

    def search(self):
        priority_queue = [(self.heuristic(self.initial_state), self.initial_state)]

        while priority_queue:
            _, current_state = heapq.heappop(priority_queue)

            if current_state not in self.visited:
                self.visited.add(current_state)

            

                for successor_state in successor(current_state):
                    heapq.heappush(priority_queue, (self.heuristic(successor_state), successor_state))
