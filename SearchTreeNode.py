
class SearchTreeNode:
    numberOfNodesCreated = 0
    def __init__(self, city, location, parent, neighbours):
        self.city = city
        self.cityCoordinates = location
        self.parent = parent
        self.neighbours = neighbours
        self.children = []

    def getCity(self):
        return self.city

    def getCoords(self):
        return self.cityCoordinates

    def getParent(self):
        return self.parent

    def getNeighbours(self):
        return self.neighbours

    def setParent(self, parent):
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)
