from SearchTreeNode import SearchTreeNode
import queue


class BreadthFirstSearch:

    def __init__(self, start, goal, cityLocations, mapCitiesToNeighbours):
        self.startCity = start
        self.goalCity = goal
        self.cityLocations = cityLocations
        self.mappingCitiesToConnectedNeighbours = mapCitiesToNeighbours
        self.allActionsTaken = []
        self.searchSolution = []
        self.numberOfNodesCreated = 0
        self.numberOfNodesVisited = 0
        self.solutionFound = False
        self.maxNumberOfNodesInMemory = 0
        self.nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }

    def breadthFirstSearch(self):
        citiesVisited = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        citiesToVisitQueue = queue.Queue()
        startCity = self.startCity

        startNode = SearchTreeNode(startCity, self.cityLocations[startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[startCity])
        self.numberOfNodesCreated = 1
        citiesToVisitQueue.put(startNode)
        self.numberOfNodesVisited = 0
        while citiesToVisitQueue.qsize() != 0:
            currentCity = citiesToVisitQueue.get()
            currentCityName = currentCity.getName()
            if currentCityName == self.goalCity:
                self.processGoal(currentCityName, currentCity.getParent())
                return self.searchSolution
            if not citiesVisited[currentCityName]:
                if currentCity.getParent():
                    self.allActionsTaken.append([currentCityName, currentCity.getParent().getCity()])
                self.numberOfNodesVisited += 1
                citiesVisited[currentCity.getCity()] = True
                listOfNeighbours = currentCity.getNeighbours()
                for neighbour in listOfNeighbours:
                    if neighbour == self.goalCity:
                        self.processGoal(neighbour, currentCity)
                        return self.searchSolution
                    if not citiesVisited[neighbour]:
                        if not self.nodeAlreadyCreated[neighbour]:
                            newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], currentCity,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            self.numberOfNodesCreated += 1
                            citiesToVisitQueue.put(newNode)
                            self.nodeAlreadyCreated[neighbour] = True
                            if self.maxNumberOfNodesInMemory < citiesToVisitQueue.qsize():
                                self.maxNumberOfNodesInMemory = citiesToVisitQueue.qsize()
        return []

    def processGoal(self, goal, parentCity):
        self.numberOfNodesVisited += 1
        pathToGoal = [goal]
        while parentCity.getParent():
            pathToGoal.append(parentCity.getCity())
            parentCity = parentCity.getParent()
        pathToGoal.append(parentCity.getCity())
        pathToGoal.reverse()
        self.searchSolution = pathToGoal
        self.solutionFound = True
