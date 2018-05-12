
class IterativeDeepeningSearch:

    def __init__(self, start, goal):
        self.startCity = start
        self.goalCity = goal
        self.visitedCities = []
        self.iterationDepth = 1
        self.searchStack = []

    def run(self):
        # run DFS for current depth limit then increate and continue

        self.iterationDepth = self.iterationDepth * 2
        self.run()
