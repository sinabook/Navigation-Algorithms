class IDS:
    def __init__(self, initial_state, max_depth):
        self.initial_state = initial_state
        self.max_depth = max_depth
        self.visited = set()

    def search(self):
        for depth in range(self.max_depth + 1):
            if self._dfs(self.initial_state, depth):
                return

    def _dfs(self, current_state, depth):
        if depth == 0:
            return

        if current_state not in self.visited:
            self.visited.add(current_state)

            

            for successor_state in successor(current_state):
                self._dfs(successor_state, depth - 1)
