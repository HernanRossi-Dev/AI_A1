from random import *
import tkinter as tk
import math
from operator import itemgetter


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



class CityMapRepresentation(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.cityLocations = []
        self.cities = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
        self.mappingCitiesToClosedNeighbours = dict()
        self.zoneNWCities = []
        self.zoneNECities = []
        self.zoneSECities = []
        self.zoneSWCities = []
        self.randomCity = []
        self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellWidth = 10
        self.cellHeight = 10
        self.cell = {}
        self.cityDrawLocations = {}
        self.cityLocations = {}
        self.cityAndNeighbours = []
        self.numberOfNeighbours = {}
        for column in range(100):
            for row in range(100):
                x1 = column * self.cellWidth
                y1 = row * self.cellHeight
                x2 = x1 + self.cellWidth
                y2 = y1 + self.cellHeight
                self.cell[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, fill='#515c6d', tags="rect")
        self.generateCityLocations()




    def generateCityLocations(self):
        shuffle(self.cities)
        self.zoneNWCities = self.cities[0:5]
        self.zoneNECities = self.cities[5:11]
        self.zoneSECities = self.cities[11:16]
        self.zoneSWCities = self.cities[16:20]
        self.randomCity = self.cities[20:]

        # NW city placement NW ranges : x = 0-50    y = 50-100
        for city in self.zoneNWCities:
            tupTemp = (randrange(0, 50, 1), randrange(50, 100, 1))
            while self.checkDistancesToAllCities(tupTemp):
                print('recalc location')
                tupTemp = (randrange(0, 50, 1), randrange(50, 100, 1))
            self.cityLocations[city] = tupTemp

        # NE city placement NE ranges : x = 50-100  y = 50-100
        for city in self.zoneNECities:
            tupTemp = (randrange(50, 100, 1), randrange(50, 100, 1))
            while self.checkDistancesToAllCities(tupTemp):
                print('recalc location')
                tupTemp = (randrange(50, 100, 1), randrange(50, 100, 1))
            self.cityLocations[city] = tupTemp

        # SE city placement SE ranges : x = 50-100  y = 0-50
        for city in self.zoneSECities:
            tupTemp = (randrange(50, 100, 1), randrange(0, 50, 1))
            while self.checkDistancesToAllCities(tupTemp):
                print('recalc location')
                tupTemp = (randrange(50, 100, 1), randrange(0, 50, 1))
            self.cityLocations[city] = tupTemp

        # SW city placement SW ranges : x = 0-50  y = 0-50
        for city in self.zoneSWCities:
            tupTemp = (randrange(0, 50, 1), randrange(0, 50, 1))
            while self.checkDistancesToAllCities(tupTemp):
                print('recalc location')
                tupTemp = (randrange(0, 50, 1), randrange(0, 50, 1))
            self.cityLocations[city] = tupTemp

        # Random city placement random ranges : x = 0-100  y = 0-100
        for city in self.randomCity:
            tupTemp = (randrange(20, 80, 1), randrange(20, 80, 1))
            while self.checkDistancesToAllCities(tupTemp):
                tupTemp = (randrange(20, 80, 1), randrange(20, 80, 1))
            self.cityLocations[city] = tupTemp

        for city, cityLocation in self.cityLocations.items():
            if city in self.numberOfNeighbours:
                if self.numberOfNeighbours[city] >= 4:
                    continue
            listOfDistancesNeighbourPairs = []
            for neighbor, neighborLocation in self.cityLocations.items():
                if city == neighbor:
                    continue
                x = (cityLocation[0] - neighborLocation[0])**2
                y = (cityLocation[1] - neighborLocation[1])**2
                z = x + y
                distance = math.sqrt(z)
                distancePair = (neighbor, distance)
                if len(self.numberOfNeighbours) == 0:
                    listOfDistancesNeighbourPairs.append(distancePair)
                elif neighbor in self.numberOfNeighbours:
                    if self.numberOfNeighbours[neighbor] >= 4:
                        continue
                    else:
                        listOfDistancesNeighbourPairs.append(distancePair)
                else:
                    listOfDistancesNeighbourPairs.append(distancePair)

            shortlistOfCities = sorted(listOfDistancesNeighbourPairs, key=lambda k: float(k[1]))
            shortlistOfCities = shortlistOfCities[0:5]
            shuffle(shortlistOfCities)


            # check if the city in the new list's neighbours already has at most 4 neighbours
            finalList = {}
            alreadyConnected = 0
            for checkIfAlreadyConnected in self.cityAndNeighbours:
                # print(checkIfAlreadyConnected)
                # print(city)
                if city in checkIfAlreadyConnected[1]:
                    # print('already connected')
                    # print(city)
                    # print(shortlistOfCities)
                    for check in shortlistOfCities:
                        if check[0] == checkIfAlreadyConnected[0]:
                            finalList[check[0]] = check[1]
                            shortlistOfCities.remove(check)
                            # print(shortlistOfCities)
                            alreadyConnected += 1
            print('city already has: ')
            print(alreadyConnected)

            upperRange = randrange(1, 5, 1)
            upperRange = upperRange - alreadyConnected
            finalList = shortlistOfCities[0:upperRange-alreadyConnected]
            for c in finalList:
                index = c[0]
                if index in self.numberOfNeighbours:
                    self.numberOfNeighbours[index] += 1
                else:
                    self.numberOfNeighbours[index] = 1

            if city in self.numberOfNeighbours:
                self.numberOfNeighbours[city] += len(finalList)
            else:
                self.numberOfNeighbours[city] = len(finalList)
            listOfNeighbours = []
            print(finalList)
            for checkNumNeigh in finalList:
                listOfNeighbours.append(checkNumNeigh[0])
            tupleCityAndNeighbours = (city, listOfNeighbours)
            self.cityAndNeighbours.append(tupleCityAndNeighbours)
            self.mappingCitiesToClosedNeighbours[city] = finalList

        for c in self.numberOfNeighbours:
            print(c, self.numberOfNeighbours[c])


        for currentCity in self.mappingCitiesToClosedNeighbours:
            currentCityCoordinates = self.cityLocations[currentCity]
            for neighborCity in self.mappingCitiesToClosedNeighbours[currentCity]:

                neighborCityCoordinates = self.cityLocations[neighborCity[0]]
                self.canvas.create_line(currentCityCoordinates[0]*10, currentCityCoordinates[1]*10,
                                        neighborCityCoordinates[0]*10, neighborCityCoordinates[1]*10,
                                        fill='green', width=1)
        for city in self.cityLocations:
            loc = self.cityLocations[city]
            self.canvas.create_text(loc[0] * 10, loc[1] * 10, anchor=tk.W, font="Arial", text=city, fill="white")


    def checkDistancesToAllCities(self, cityLocation):
        for neighbor, neighborLocation in self.cityLocations.items():
            x = (cityLocation[0] - neighborLocation[0]) ** 2
            y = (cityLocation[1] - neighborLocation[1]) ** 2
            z = x + y
            distance = math.sqrt(z)
            if distance < 5:
                return True
        return False
