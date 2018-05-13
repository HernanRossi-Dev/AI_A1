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


    def depthFirstSearch(self):
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        stack = [startNode]
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        while stack:
            city = stack.pop()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
                print('Visiting Goal', cityName)
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                print('Number of nodes created')
                print(self.numberOfNodesCreated)
                print('Number of Nodes Visited')
                print(self.numberOfCitiesVisited)
                print('Path to goal found: ')
                print(self.searchSolution)
                self.solutionFound = True
                return self.searchSolution
            if cityName not in visited:
                print('Visiting ', city.getCity())
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                for neighbour in cityNeighbours:
                    newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                             self.mappingCitiesToConnectedNeighbours[neighbour])
                    stack.append(newNode)
                    self.numberOfNodesCreated += 1
            else:
                # already visited
                continue
        print('No solution Found.')
        return []