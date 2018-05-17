import math
from SearchTreeNode import SearchTreeNode
import queue
class stateTuple(object):
    def __init__(self, priority, state):
        self.priority = priority
        self.state = state
        return
    def __eq__(self, other):
        return not self.priority < other.priority and not other.priority < self.priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __gt__(self, other):
        return  other.priority < self.priority

class GreedyBestFirst:

    def __init__(self, start, goal, cityLocations, mapCitiesToNeighbours):
        self.startCity = start
        self.goalCity = goal
        self.cityLocations = cityLocations
        self.mappingCitiesToConnectedNeighbours = mapCitiesToNeighbours
        self.allActionsTaken = []
        self.searchSolution = []
        self.numberOfNodesCreated = 0
        self.numberOfCitiesVisited = 0
        self.solutionFound = False
        self.maxNumberOfNodesInMemory = 0
        self.cities = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
        self.mapCitiesToDistanceToGoalEuclideanDist = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
            'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
            'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
            'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
            'Y': 0, 'Z': 0
        }
        self.mapCitiesToDistanceToGoalManhattanDist = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
            'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
            'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
            'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
            'Y': 0, 'Z': 0
        }
        self.calcAllCityDistToGoalEuclidean()
        self.calcAllCityDistanceToGoalManhattanDistance()


    def greedyBestFirstSearchEuclidean(self):
        nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        priorityQueue = queue.PriorityQueue()
        tup = stateTuple(0.0, startNode)
        priorityQueue.put(tup)
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        self.maxNumberOfNodesInMemory = 0

        while not priorityQueue.empty():
            cityTuple = priorityQueue.get()
            city = cityTuple.state
            if self.maxNumberOfNodesInMemory < priorityQueue.qsize():
                self.maxNumberOfNodesInMemory = priorityQueue.qsize()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                self.solutionFound = True
                return self.searchSolution
            if cityName not in visited:
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                for neighbour in cityNeighbours:
                    if not nodeAlreadyCreated[neighbour]:
                        if neighbour not in visited:
                            costToGoal = self.mapCitiesToDistanceToGoalEuclideanDist[neighbour]
                            newNode = SearchTreeNode(neighbour,
                                                     self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            nodeAlreadyCreated[neighbour] = True
                            self.numberOfNodesCreated += 1
                            heuristicCost =  costToGoal
                            tup = stateTuple(heuristicCost, newNode)
                            priorityQueue.put(tup)
        return []

    def greedyBestFirstSearchNoHeuristic(self):
            self.allActionsTaken = []
            self.searchSolution = []
            self.solutionFound = False
            visited = []
            startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                       self.mappingCitiesToConnectedNeighbours[self.startCity])
            stack = [startNode]
            self.numberOfNodesCreated = 1
            self.numberOfCitiesVisited = 0
            self.maxNumberOfNodesInMemory = 0

            while stack:
                city = stack.pop()
                cityName = city.getName()
                if self.maxNumberOfNodesInMemory < len(stack):
                    self.maxNumberOfNodesInMemory = len(stack)
                if city.getParent():
                    self.allActionsTaken.append([cityName, city.getParent().getCity()])
                if cityName == self.goalCity:
                    self.processGoal(cityName, city.getParent())
                    return self.searchSolution
                if cityName not in visited:
                    visited.append(cityName)
                    self.numberOfCitiesVisited += 1
                    cityNeighbours = city.getNeighbours()
                    for neighbour in cityNeighbours:
                        if neighbour not in visited:
                            newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            stack.append(newNode)
                            self.numberOfNodesCreated += 1
            return []


    def greedyBestFirstSearchManhattan(self):
        nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        priorityQueue = queue.PriorityQueue()
        tup = stateTuple(0.0, startNode)
        priorityQueue.put(tup)
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        self.maxNumberOfNodesInMemory = 0

        while not priorityQueue.empty():
            cityTuple = priorityQueue.get()
            city = cityTuple.state
            if self.maxNumberOfNodesInMemory < priorityQueue.qsize():
                self.maxNumberOfNodesInMemory = priorityQueue.qsize()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                self.solutionFound = True
                return self.searchSolution
            if cityName not in visited:
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                for neighbour in cityNeighbours:
                    if not nodeAlreadyCreated[neighbour]:
                        if neighbour not in visited:
                            costToGoal = self.mapCitiesToDistanceToGoalManhattanDist[neighbour]
                            newNode = SearchTreeNode(neighbour,
                                                     self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            nodeAlreadyCreated[neighbour] = True
                            self.numberOfNodesCreated += 1
                            heuristicCost = costToGoal
                            tup = stateTuple(heuristicCost, newNode)
                            priorityQueue.put(tup)
        return []

    def processGoal(self, goal, parentCity):
        self.numberOfCitiesVisited += 1
        pathToGoal = [goal]
        while parentCity.getParent():
            pathToGoal.append(parentCity.getCity())
            parentCity = parentCity.getParent()
        pathToGoal.append(parentCity.getCity())
        pathToGoal.reverse()
        self.searchSolution = pathToGoal
        self.solutionFound = True

    def calcAllCityDistToGoalEuclidean(self):
        goalLocation = self.cityLocations[self.goalCity]
        for city in self.cities:
            currentCityLocation = self.cityLocations[city]
            x = (currentCityLocation[0] - goalLocation[0]) ** 2
            y = (currentCityLocation[1] - goalLocation[1]) ** 2
            z = x + y
            distance = math.sqrt(z)
            self.mapCitiesToDistanceToGoalEuclideanDist[city] = distance

    def calcAllCityDistanceToGoalManhattanDistance(self):
        goalLocation = self.cityLocations[self.goalCity]
        for city in self.cities:
            currentCityLocation = self.cityLocations[city]
            x = abs(currentCityLocation[0] - goalLocation[0])
            y = abs(currentCityLocation[1] - goalLocation[1])
            distance = x + y
            self.mapCitiesToDistanceToGoalManhattanDist[city] = distance