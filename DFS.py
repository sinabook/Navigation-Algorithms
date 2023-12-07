class DFS:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.visited = set()

    def search(self):
        self._dfs(self.initial_state)

    def _dfs(self, current_state):
        if current_state not in self.visited:
            self.visited.add(current_state)

            
            for successor_state in successor(current_state):
                self._dfs(successor_state)
