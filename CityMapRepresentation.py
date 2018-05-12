from random import *
import math
import queue
from PrintMap import PrintMap
from SearchTreeNode import SearchTreeNode

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
            # upperRange = upperRange - numberOfNeighbours
            finalList = shortlistOfCities[0:upperRange]

            for connectNeighbour in finalList:
                if connectNeighbour[0] in self.mappingCitiesToConnectedNeighbours[city]:
                    continue
                else:
                    self.mappingCitiesToConnectedNeighbours[city].append(connectNeighbour[0])
                    self.mappingCitiesToConnectedNeighbours[connectNeighbour[0]].append(city)

        sumNumNeighbours = 0
        for cityWithNeighbours in self.mappingCitiesToConnectedNeighbours:
            # print(cityWithNeighbours, self.mappingCitiesToConnectedNeighbours[cityWithNeighbours])
            currentNumNeighbours = len(self.mappingCitiesToConnectedNeighbours[cityWithNeighbours])
            sumNumNeighbours += currentNumNeighbours

        averageNumBranches = sumNumNeighbours /26
        # print('The average Number of branches is : ')
        # print(averageNumBranches)
        # return averageNumBranches
        self.BreadthFirstSearch()


    def checkDistancesToAllCities(self, cityLocation):
        for neighbor, neighborLocation in self.cityLocations.items():
            x = (cityLocation[0] - neighborLocation[0]) ** 2
            y = (cityLocation[1] - neighborLocation[1]) ** 2
            z = x + y
            distance = math.sqrt(z)
            if distance < 15:
                return True
        return False

    def BreadthFirstSearch(self):
        numberOfNodesCreated = 0
        citiesVisited = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        citiesToVisitQueue = queue.Queue()
        startCity = self.startCity

        startNode = SearchTreeNode(startCity, self.cityLocations[startCity], '', self.mappingCitiesToConnectedNeighbours[startCity])
        # startNode.numberOfNodesCreated = startNode.numberOfNodesCreated + 1
        numberOfNodesCreated +=1
        citiesToVisitQueue.put(startNode)

        while citiesToVisitQueue.qsize() != 0:
            visitCity = citiesToVisitQueue.get()
            print('Visiting ', visitCity.getCity())

            if visitCity.getCity() == self.goalCity:
            # get goal path by going back through all of the goal nodes ancestors
                pathToGoal = []
                while visitCity.getParent() != '':
                    pathToGoal.append(visitCity.getCity())
                    visitCity = visitCity.getParent()
                pathToGoal.append(visitCity.getCity())
                pathToGoal.reverse()
                print('Number of nodes created')
                print(numberOfNodesCreated)
                print('Path to goal found: ')
                print(pathToGoal)
                return pathToGoal
            if citiesVisited[visitCity.getCity()]:
                numberOfNodesCreated -= 1
                continue
            else:
                citiesVisited[visitCity.getCity()] = True
                listOfNeighbours = visitCity.getNeighbours()
                for neighbour in listOfNeighbours:
                    newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], visitCity, self.mappingCitiesToConnectedNeighbours[neighbour])
                    # newNode.numberOfNodesCreated = newNode.numberOfNodesCreated + 1
                    numberOfNodesCreated += 1
                    citiesToVisitQueue.put(newNode)
