from random import *
import math
from PrintMap import PrintMap
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from IterativeDeepeningSearch import IterativeDeepeningSearch
import sys

class CityMapRepresentation:

    def __init__(self):
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
        # print('Start city is: ')
        # print(self.startCity)
        # print('Goal city is: ')
        # print(self.goalCity)

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
        # print('The average Number of branches is : ')
        # print(averageNumBranches)
        return averageNumBranches
