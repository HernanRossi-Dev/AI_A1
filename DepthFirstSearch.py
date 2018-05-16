from SearchTreeNode import SearchTreeNode


class DepthFirstSearch:

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
        self.visited = []
        self.NodesInMemory = 0
        self.nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }

    def depthFirstSearchIterative(self):
        self.nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.numberOfNodesCreated = 0
        self.numberOfCitiesVisited = 0
        self.solutionFound = False
        self.maxNumberOfNodesInMemory = 0
        self.visited = []
        self.NodesInMemory = 0
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        stack = [startNode]
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        while stack:
            city = stack.pop()
            if self.maxNumberOfNodesInMemory < len(stack):
                self.maxNumberOfNodesInMemory = len(stack)
            cityName = city.getName()
            if cityName == self.goalCity:
                self.processGoal(city)
                return self.searchSolution
            if cityName not in self.visited:
                if city.getParent():
                    self.allActionsTaken.append([cityName, city.getParent().getCity()])
                self.visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                for neighbour in cityNeighbours:
                    if neighbour not in self.visited:
                        if not self.nodeAlreadyCreated[neighbour]:
                            newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                                 self.mappingCitiesToConnectedNeighbours[neighbour])
                            stack.append(newNode)
                            self.nodeAlreadyCreated[neighbour] = True
                            self.numberOfNodesCreated += 1
        return []

    def runRecursiveDepthFirstSearch(self):
        self.nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.numberOfNodesCreated = 0
        self.numberOfCitiesVisited = 0
        self.solutionFound = False
        self.maxNumberOfNodesInMemory = 0
        self.NodesInMemory = 0
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        self.visited = []
        self.RecursiveDepthFirstSearch(startNode)

    def RecursiveDepthFirstSearch(self, city):
        cityName = city.getName()
        if self.maxNumberOfNodesInMemory < self.NodesInMemory:
            self.maxNumberOfNodesInMemory = self.NodesInMemory
        if cityName == self.goalCity:
            self.processGoal(city)
            return self.searchSolution
        if  cityName not in self.visited:
            self.visited.append(cityName)
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            self.numberOfCitiesVisited += 1
            cityNeighbours = city.getNeighbours()
            for neighbour in cityNeighbours:
                if neighbour not in self.visited:
                    if not self.nodeAlreadyCreated[neighbour]:
                        newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                             self.mappingCitiesToConnectedNeighbours[neighbour])
                        self.numberOfNodesCreated += 1
                        self.NodesInMemory += 1
                        self.nodeAlreadyCreated[neighbour] = True
                        self.RecursiveDepthFirstSearch(newNode)
                        self.NodesInMemory -= 1
        return

    def processGoal(self, visitCity):
        self.numberOfCitiesVisited += 1
        pathToGoal = []
        while visitCity.getParent():
            pathToGoal.append(visitCity.getCity())
            visitCity = visitCity.getParent()
        pathToGoal.append(visitCity.getCity())
        pathToGoal.reverse()
        self.searchSolution = pathToGoal
        self.solutionFound = True