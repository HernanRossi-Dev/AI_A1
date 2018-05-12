import tkinter as tk

class PrintMap(tk.Tk):

    def __init__(self, mapping, start, goal, cityLocations, *args, **kwargs):
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
        self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
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
                                        fill='#C1AA9D', width=1)
        for city in self.cityLocations:
            loc = self.cityLocations[city]
            self.canvas.create_text(loc[0] * 10, loc[1] * 10, anchor=tk.W, font="Arial", text=city, fill="white")
        startCityLocation = self.cityLocations[self.startCity]
        goalCityLocation = self.cityLocations[self.goalCity]
        self.canvas.create_oval(startCityLocation[0] * 10 - 25, startCityLocation[1] * 10 - 25,
                                startCityLocation[0] * 10 + 30, startCityLocation[1] * 10 + 30, outline='#46b400')
        self.canvas.create_oval(goalCityLocation[0] * 10 - 25, goalCityLocation[1] * 10 - 25,
                                goalCityLocation[0] * 10 + 30, goalCityLocation[1] * 10 + 30, outline='#c10000')