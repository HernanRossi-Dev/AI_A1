from random import *
import math
from PrintMap import PrintMap
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from IterativeDeepeningSearch import IterativeDeepeningSearch
import sys

#     NorthWest region is :
#                           top left corner = (0, 100)          top right corner = (50, 100)
#                         bottom left corner = (0, 50)        Bottom right corner = (50, 50)
#     NorthEast region is :
#                           top left corner = (50, 100)          top right corner = (100, 100)
#                         bottom left corner = (50, 50)        Bottom right corner = (100, 50)
#     SouthEast region is :
#                            top left corner = (50, 50)          top right corner = (100, 50)
#                          bottom left corner = (50, 0)        Bottom right corner = (100, 0)
#     SouthWest region is :
#                           top left corner = (0, 50)          top right corner = (50, 50)
#                         bottom left corner = (0, 0)        Bottom right corner = (50, 0)
#   NW ranges : x = 0-50    y = 50-100
#   NE ranges : x = 50-100  y = 50-100
#   SE ranges : x = 50-100  y = 0-50
#   SW ranges : x = 0-50  y = 0-50
#
# A city is in location based on its SW: if it is in location (50,50) it will be in quadrant NE
#     create dictionary of city location pairs

class CityMapRepresentation:

    def __init__(self, *args, **kwargs):
        self.cities = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
        self.mappingCitiesToConnectedNeighbours = {
            'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [],
            'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [],
            'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [],
            'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [],
            'Y': [], 'Z': []
        }
        self.startCity = ''
        self.goalCity = ''
        self.cityLocations = {}
        self.searchSolution = []
        self.allActionsTaken = []
        self.printMap = None

    @staticmethod
    def getEuclideanDistance(fromCity, toCity):
        x = (fromCity[0] - toCity[0]) ** 2
        y = (fromCity[1] - toCity[1]) ** 2
        z = x + y
        return math.sqrt(z)

    def generateStateConditions(self):
        startCityIndex = randrange(0, 25, 1)
        goalCityIndex = randrange(0, 25, 1)
        while startCityIndex == goalCityIndex:
            goalCityIndex = randrange(0, 25, 1)
        self.startCity = self.cities[startCityIndex]
        self.goalCity = self.cities[goalCityIndex]
        print('Start city is: ')
        print(self.startCity)
        print('Goal city is: ')
        print(self.goalCity)

    def generateCityLocations(self):
        self.generateStateConditions()
        shuffle(self.cities)
        for city in self.cities:
            tupTemp = (randrange(0, 100, 1), randrange(0, 100, 1))
            while self.checkDistancesToAllCities(tupTemp):
                tupTemp = (randrange(0, 100, 1), randrange(0, 100, 1))
            self.cityLocations[city] = tupTemp
        for i in range(0, 25):
            city = self.cities[i]
            cityLocation = self.cityLocations[city]
            listOfDistancesNeighbourPairs = []
            currentCityListOfNeighbours = self.mappingCitiesToConnectedNeighbours[city]
            if len(currentCityListOfNeighbours) > 3:
                continue
            for j in range(0, 25):
                neighbor = self.cities[25-j]
                if city == neighbor:
                    continue
                neighborLocation = self.cityLocations[neighbor]
                CandidateCityListOfNeighbours = self.mappingCitiesToConnectedNeighbours[neighbor]
                if len(CandidateCityListOfNeighbours) > 3:
                    continue

                distance = self.getEuclideanDistance(cityLocation, neighborLocation)
                distancePair = (neighbor, distance)

                listOfDistancesNeighbourPairs.append(distancePair)
            shortlistOfCities = sorted(listOfDistancesNeighbourPairs, key=lambda k: float(k[1]))
            shortlistOfCities = shortlistOfCities[0:5]
            shuffle(shortlistOfCities)
            numberOfNeigboursAlreadyConnected = len(self.mappingCitiesToConnectedNeighbours[city])
            upperRange = randrange(1, 5 - numberOfNeigboursAlreadyConnected, 1)
            finalList = shortlistOfCities[0:upperRange]

            for connectNeighbour in finalList:
                if connectNeighbour[0] in self.mappingCitiesToConnectedNeighbours[city]:
                    continue
                else:
                    self.mappingCitiesToConnectedNeighbours[city].append(connectNeighbour[0])
                    self.mappingCitiesToConnectedNeighbours[connectNeighbour[0]].append(city)

        # if len(sys.argv) < 2:
        #     print('Must supply type of search to perform')
        #     exit(0)
        # if sys.argv[1] == 'DFS':
        #     runDFS = DepthFirstSearch(self.startCity, self.goalCity, self.cityLocations, self.mappingCitiesToConnectedNeighbours)
        #     runDFS.depthFirstSearch()
        #     self.allActionsTaken = runDFS.allActionsTaken
        #     self.searchSolution = runDFS.searchSolution
        # elif sys.argv[1] == 'IDS':
        #     runIDS = IterativeDeepeningSearch(self.startCity, self.goalCity, self.cityLocations, self.mappingCitiesToConnectedNeighbours)
        #     runIDS.iterativeDS()
        #     self.allActionsTaken = runIDS.allActionsTaken
        #     self.searchSolution = runIDS.searchSolution
        # elif sys.argv[1] == 'BFS':
        #     runBFS = BreadthFirstSearch(self.startCity, self.goalCity, self.cityLocations, self.mappingCitiesToConnectedNeighbours)
        #     runBFS.breadthFirstSearch()
        #     self.allActionsTaken = runBFS.allActionsTaken
        #     self.searchSolution = runBFS.searchSolution
        # elif sys.argv[1] =='IDS100':
        #     numberProbsSolved = 0
        #     sumNodesCreated = 0
        #     sumNodesVisited = 0
        #     sumSolutionLength = 0
        #     for i in range(0, 99):
        #         runIDS = IterativeDeepeningSearch(self.startCity, self.goalCity, self.cityLocations,
        #                                           self.mappingCitiesToConnectedNeighbours)
        #         runIDS.iterativeDS()
        #         numberNodesCreated = runIDS.numberOfNodesCreated
        #         numberNodesVisited = runIDS.numberOfCitiesVisited
        #         solutionFound = runIDS.solutionFound
        #         solutionPath = runIDS.searchSolution
        #         solutionLength = len(solutionPath)
        #         if solutionFound:
        #             numberProbsSolved += 1
        #         sumNodesCreated += numberNodesCreated
        #         sumNodesVisited += numberNodesVisited
        #         sumSolutionLength += solutionLength
        #
        #
        #     aveNodesCreated = sumNodesCreated / 100
        #     aveNodesVisited = sumNodesVisited / 100
        #     aveSolutonLength = sumSolutionLength / 100
        #     print('Average Nodes Visited: ', aveNodesVisited)
        #     print('Average Nodes Created: ', aveNodesCreated)
        #     print('Average Solution Length: ', aveSolutonLength)
        #     print('Number problems Solved: ', numberProbsSolved)
        #
        # elif sys.argv[1] =='DFS100':
        #     numberProbsSolved = 0
        #     sumNodesCreated = 0
        #     sumNodesVisited = 0
        #     sumSolutionLength = 0
        #     for i in range(0, 99):
        #         runDFS = DepthFirstSearch(self.startCity, self.goalCity, self.cityLocations,
        #                                   self.mappingCitiesToConnectedNeighbours)
        #         runDFS.depthFirstSearch()
        #         numberNodesCreated = runDFS.numberOfNodesCreated
        #         numberNodesVisited = runDFS.numberOfCitiesVisited
        #         solutionFound = runDFS.solutionFound
        #         solutionPath = runDFS.searchSolution
        #         solutionLength = len(solutionPath)
        #         if solutionFound:
        #             numberProbsSolved += 1
        #         sumNodesCreated += numberNodesCreated
        #         sumNodesVisited += numberNodesVisited
        #         sumSolutionLength += solutionLength
        #
        #
        #     aveNodesCreated = sumNodesCreated / 100
        #     aveNodesVisited = sumNodesVisited / 100
        #     aveSolutonLength = sumSolutionLength / 100
        #     print('Average Nodes Visited: ', aveNodesVisited)
        #     print('Average Nodes Created: ', aveNodesCreated)
        #     print('Average Solution Length: ', aveSolutonLength)
        #     print('Number problems Solved: ', numberProbsSolved)


        # if len(sys.argv) < 3:
        #     print('Not printing map')
        # elif sys.argv[2] == 'print':
        #     self.printMap = PrintMap(self.mappingCitiesToConnectedNeighbours, self.startCity, self.goalCity,
        #                               self.cityLocations, self.searchSolution, self.allActionsTaken)
        #     self.printMap.mainloop()

    def checkDistancesToAllCities(self, cityLocation):
        for neighbor, neighborLocation in self.cityLocations.items():
            x = (cityLocation[0] - neighborLocation[0]) ** 2
            y = (cityLocation[1] - neighborLocation[1]) ** 2
            z = x + y
            distance = math.sqrt(z)
            if distance < 15:
                return True
        return False

    def calcAverageBranches(self):
        sumNumNeighbours = 0
        for cityWithNeighbours in self.mappingCitiesToConnectedNeighbours:
            # print(cityWithNeighbours, self.mappingCitiesToConnectedNeighbours[cityWithNeighbours])
            currentNumNeighbours = len(self.mappingCitiesToConnectedNeighbours[cityWithNeighbours])
            sumNumNeighbours += currentNumNeighbours
        averageNumBranches = sumNumNeighbours /26
        print('The average Number of branches is : ')
        print(averageNumBranches)
        return averageNumBranches
