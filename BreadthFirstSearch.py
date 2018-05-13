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
            visitCity = citiesToVisitQueue.get()

            if visitCity.getParent():
                self.allActionsTaken.append([visitCity.getCity(), visitCity.getParent().getCity()])

            if visitCity.getCity() == self.goalCity:
                self.numberOfNodesVisited += 1
                print('Visiting Goal', visitCity.getCity())
                pathToGoal = []
                while visitCity.getParent():
                    pathToGoal.append(visitCity.getCity())
                    visitCity = visitCity.getParent()
                pathToGoal.append(visitCity.getCity())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                print('Number of nodes created')
                print(self.numberOfNodesCreated)
                print('Number of Nodes Visited')
                print(self.numberOfNodesVisited)
                print('Path to goal found: ')
                print(self.searchSolution)
                self.solutionFound = True
                return self.searchSolution
            if citiesVisited[visitCity.getCity()]:
                continue
            else:
                self.numberOfNodesVisited += 1
                print('Visiting ', visitCity.getCity())
                citiesVisited[visitCity.getCity()] = True
                listOfNeighbours = visitCity.getNeighbours()
                for neighbour in listOfNeighbours:
                    newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], visitCity,
                                             self.mappingCitiesToConnectedNeighbours[neighbour])
                    self.numberOfNodesCreated += 1
                    citiesToVisitQueue.put(newNode)

        # No solution found return an empty path
        print('No solution Found')
        return []