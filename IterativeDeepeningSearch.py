import sys
from SearchTreeNode import SearchTreeNode

class IterativeDeepeningSearch:

    def __init__(self, start, goal, cityLocations, mapCitiesToNeighbours):
        self.startCity = start
        self.goalCity = goal
        self.numberOfNodesCreated = 0
        self.numberOfCitiesVisited = 0
        self.cityLocations = cityLocations
        self.mappingCitiesToConnectedNeighbours = mapCitiesToNeighbours
        self.allActionsTaken = []
        self.searchSolution = []
        self.visitedCities = []
        self.solutionFound = False
        self.maxNumberOfNodesInMemory = 0
        self.nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }


    def iterativeDS(self):
        for depth in range(1, 100):
            self.allActionsTaken = []
            self.searchSolution = []
            self.visitedCities = []
            self.nodeAlreadyCreated = {
                'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
                'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
                'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
                'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
                'Y': False, 'Z': False
            }
            result = self.depthLimit(depth)
            if result != 'Continue':
                return 'Solution Found'
        return 'No Solution Found'

    def depthLimit(self, limit):
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity], 0)
        stack = [startNode]
        numberOfNodesCreated = 1
        numberOfCitiesVisited = 0
        while stack:
            if self.maxNumberOfNodesInMemory < len(stack):
                self.maxNumberOfNodesInMemory = len(stack)
            city = stack.pop()
            cityName = city.getName()
            if cityName == self.goalCity:
                numberOfCitiesVisited += 1
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                self.numberOfNodesCreated = numberOfNodesCreated
                self.numberOfCitiesVisited = numberOfCitiesVisited
                self.solutionFound = True
                return 'Solution Found'
            if cityName not in visited:
                if city.getParent():
                    self.allActionsTaken.append([cityName, city.getParent().getCity()])
                if city.depth >= limit:
                    visited.append(cityName)
                    numberOfCitiesVisited += 1
                else:
                    visited.append(cityName)
                    numberOfCitiesVisited += 1
                    cityNeighbours = city.getNeighbours()
                    for neighbour in cityNeighbours:
                        if neighbour == self.goalCity:
                            numberOfCitiesVisited += 1
                            pathToGoal = [neighbour]
                            while city.getParent():
                                pathToGoal.append(city.getName())
                                city = city.getParent()
                            pathToGoal.append(city.getName())
                            pathToGoal.reverse()
                            self.searchSolution = pathToGoal
                            self.numberOfNodesCreated = numberOfNodesCreated
                            self.numberOfCitiesVisited = numberOfCitiesVisited
                            self.solutionFound = True
                            return 'Solution Found'
                        if neighbour not in visited:
                            if self.nodeAlreadyCreated[neighbour]:
                                continue
                            else:
                                newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour], city.depth + 1)
                                stack.append(newNode)
                                self.nodeAlreadyCreated[neighbour] = True
                                numberOfNodesCreated += 1
            else:
                continue
        return 'Continue'

