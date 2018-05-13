
class SearchTreeNode:
    numberOfNodesCreated = 0

    def __init__(self, city, location, parent, neighbours, depth = 0):
        self.city = city
        self.cityCoordinates = location
        self.parent = parent
        self.neighbours = neighbours
        self.children = []
        self.depth = depth

    def getCity(self):
        return self.city

    def getName(self):
        return self.city

    def getCoords(self):
        return self.cityCoordinates

    def getParent(self):
        return self.parent

    def getNeighbours(self):
        return self.neighbours

    def setParent(self, parent):
        self.parent = parent

    def getDepth(self):
        return self.depth

    def addChild(self, child):
        self.children.append(child)
