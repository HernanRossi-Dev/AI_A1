import tkinter as tk


class PrintMap(tk.Tk):

    def __init__(self, mapping, start, goal, cityLocations, searchSolution, allCitiesVisited, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.cities = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
        self.mappingCitiesToConnectedNeighbours = mapping
        self.startCity = start
        self.goalCity = goal
        self.cityLocations = cityLocations
        self.searchSolution = searchSolution
        self.allCitiesVisited = allCitiesVisited
        self.canvas = tk.Canvas(self, width=1300, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellWidth = 10
        self.cellHeight = 10
        self.cell = {}
        self.cityDrawLocations = {}

        for column in range(100):
            for row in range(100):
                x1 = column * self.cellWidth
                y1 = row * self.cellHeight
                x2 = x1 + self.cellWidth
                y2 = y1 + self.cellHeight
                self.cell[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, fill='#515c6d', tags="rect")
        self.printMap()


    def printMap(self):
        for currentCity in self.cities:
            currentCityCoordinates = self.cityLocations[currentCity]
            for neighborCity in self.mappingCitiesToConnectedNeighbours[currentCity]:
                neighborCityCoordinates = self.cityLocations[neighborCity]
                self.canvas.create_line(currentCityCoordinates[0] * 10, currentCityCoordinates[1] * 10,
                                        neighborCityCoordinates[0] * 10, neighborCityCoordinates[1] * 10,
                                        fill='#a8a6a6', width=1)

        startCityLocation = self.cityLocations[self.startCity]
        goalCityLocation = self.cityLocations[self.goalCity]
        self.canvas.create_oval(startCityLocation[0] * 10 - 25, startCityLocation[1] * 10 - 25,
                                startCityLocation[0] * 10 + 30, startCityLocation[1] * 10 + 30, outline='#46b400')
        self.canvas.create_oval(goalCityLocation[0] * 10 - 25, goalCityLocation[1] * 10 - 25,
                                goalCityLocation[0] * 10 + 30, goalCityLocation[1] * 10 + 30, outline='#c10000')
        self.printAllCitiesVisited()
        self.printSearchSolution()
        for city in self.cityLocations:
            loc = self.cityLocations[city]
            self.canvas.create_text(loc[0] * 10, loc[1] * 10, anchor=tk.W, font="Arial", text=city, fill="white")

    def printSearchSolution(self):
        toCity = False
        for city in self.searchSolution:
            if toCity:
                fromCity = city
                fromCityLocation = self.cityLocations[fromCity]
                toCityLocation = self.cityLocations[toCity]
                self.canvas.create_line(fromCityLocation[0] * 10, fromCityLocation[1] * 10, toCityLocation[0] * 10,
                                        toCityLocation[1] * 10, fill='#017720', width=3)
            toCity = city

    def printAllCitiesVisited(self):
        actionNumber = 0
        textOffset = 0
        yOffset = 1025
        citiesTagged = {}
        for toCity, fromCity in self.allCitiesVisited:
            fromCityLocation = self.cityLocations[fromCity]
            toCityLocation = self.cityLocations[toCity]
            actionNumber += 1
            # if fromCity in citiesTagged:
            #     citiesTagged[fromCity] += 15
            # else:
            #     citiesTagged[fromCity] = 25
            textOffset += 25
            if actionNumber == 40:
                textOffset = 25
                yOffset = yOffset + 150
            outputString = 'Move: ' + str(actionNumber) + ' ' + fromCity + ' -> ' + toCity
            self.canvas.create_line(fromCityLocation[0] * 10, fromCityLocation[1] * 10, toCityLocation[0] * 10,
                                        toCityLocation[1] * 10, fill='#a36501', width=3)
            # self.canvas.create_text((fromCityLocation[0] * 10),  fromCityLocation[1] * 10 + 20 + citiesTagged[fromCity], anchor=tk.W, font="Arial", text=outputString, fill="white")
            self.canvas.create_text(yOffset,  textOffset , anchor=tk.W, font="Arial", text=outputString, fill="black")

