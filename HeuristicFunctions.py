class HeuristicFunctions:
    @staticmethod
    def simple_heuristic(state):
        distances = [abs(state.x - goal.x) + abs(state.y - goal.y) for goal in goals]
        return sum(distances)
