from CityMapRepresentation import CityMapRepresentation
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from IterativeDeepeningSearch import IterativeDeepeningSearch
import sys
from PrintMap import PrintMap
import time
import math

class UninformedSearch:

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

    def run(self, arg):
        if arg == 'DFS':
            newMap = CityMapRepresentation()
            newMap.generateCityLocations()
            self.startCity = newMap.startCity
            self.goalCity = newMap.goalCity
            self.cityLocations = newMap.cityLocations
            self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
            runDFS = DepthFirstSearch( self.startCity, self.goalCity, self.cityLocations,
                                       self.mappingCitiesToConnectedNeighbours)
            runDFS.depthFirstSearchIterative()
            self.allActionsTaken = runDFS.allActionsTaken
            self.searchSolution = runDFS.searchSolution
            lengthOfSolutionExactDistance = self.calcLengthOfSolution(runDFS.searchSolution)

            print('Running DFS iteratively')
            print('Number of Nodes Visited: ', runDFS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runDFS.numberOfNodesCreated)
            print('Max number of Nodes in Memory: ', runDFS.maxNumberOfNodesInMemory)
            print('Number of cities visited in Solution: ', len(runDFS.searchSolution))
            print('The resulting path is: ', runDFS.searchSolution)

            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)
            print (' ')
        if arg == 'DFSrec':
            newMap = CityMapRepresentation()
            newMap.generateCityLocations()
            self.startCity = newMap.startCity
            self.goalCity = newMap.goalCity
            self.cityLocations = newMap.cityLocations
            self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
            runDFS = DepthFirstSearch( self.startCity, self.goalCity, self.cityLocations,
                                       self.mappingCitiesToConnectedNeighbours)
            runDFS.runRecursiveDepthFirstSearch()
            self.allActionsTaken = runDFS.allActionsTaken
            self.searchSolution = runDFS.searchSolution
            lengthOfSolutionExactDistance = self.calcLengthOfSolution(runDFS.searchSolution)

            print('Running DFS iteratively')
            print('Number of Nodes Visited: ', runDFS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runDFS.numberOfNodesCreated)
            print('Max number of Nodes in Memory: ', runDFS.maxNumberOfNodesInMemory)
            print('Number of cities visited in Solution: ', len(runDFS.searchSolution))
            print('The resulting path is: ', runDFS.searchSolution)
            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)
        elif arg == 'IDS':
            newMap = CityMapRepresentation()
            newMap.generateCityLocations()
            self.startCity = newMap.startCity
            self.goalCity = newMap.goalCity
            self.cityLocations = newMap.cityLocations
            self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
            runIDS = IterativeDeepeningSearch(self.startCity, self.goalCity, self.cityLocations,
                                              self.mappingCitiesToConnectedNeighbours)
            runIDS.iterativeDS()
            self.allActionsTaken = runIDS.allActionsTaken
            self.searchSolution = runIDS.searchSolution
            lengthOfSolutionExactDistance = self.calcLengthOfSolution(runIDS.searchSolution)

            print('Number of Nodes Visited: ', runIDS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runIDS.numberOfNodesCreated)
            print('Max number of Nodes in Memory: ', runIDS.maxNumberOfNodesInMemory)

            print('Number of cities visited in Solution: ', len(runIDS.searchSolution))
            print('The resulting path is: ', runIDS.searchSolution)
            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)

        elif arg == 'BFS':
            newMap = CityMapRepresentation()
            newMap.generateCityLocations()
            self.startCity = newMap.startCity
            self.goalCity = newMap.goalCity
            self.cityLocations = newMap.cityLocations
            self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
            runBFS = BreadthFirstSearch(self.startCity, self.goalCity, self.cityLocations,
                                        self.mappingCitiesToConnectedNeighbours)
            runBFS.breadthFirstSearch()
            self.allActionsTaken = runBFS.allActionsTaken
            self.searchSolution = runBFS.searchSolution
            lengthOfSolutionExactDistance = self.calcLengthOfSolution(runBFS.searchSolution)

            print('Number of Nodes Visited: ', runBFS.numberOfNodesVisited)
            print('Number of Nodes Created: ', runBFS.numberOfNodesCreated)
            print('Max number of Nodes in Memory: ', runBFS.maxNumberOfNodesInMemory)
            print('Number of cities visited in Solution: ', len(runBFS.searchSolution))
            print('The resulting path is: ', runBFS.searchSolution)
            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)

        elif arg == 'IDS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0
            sumAverageNodeInMemory = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                sumAverageBranches += newMap.calcAverageBranches()
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                runIDS = IterativeDeepeningSearch(self.startCity, self.goalCity, self.cityLocations,
                                                  self.mappingCitiesToConnectedNeighbours)
                runIDS.iterativeDS()
                numberNodesCreated = runIDS.numberOfNodesCreated
                numberNodesVisited = runIDS.numberOfCitiesVisited
                solutionFound = runIDS.solutionFound
                solutionPath = runIDS.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumLengthOfSolution += self.calcLengthOfSolution(runIDS.searchSolution)
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumAverageNodeInMemory += runIDS.maxNumberOfNodesInMemory

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches /100
            aveLengthOfSolution = sumLengthOfSolution / 100
            averageNodesInMemory = sumAverageNodeInMemory / 100

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Nodes in Memory: ', averageNodesInMemory)

            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)
            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ' , elapsed_time)
        elif arg == 'DFS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0
            sumAverageNodeInMemory = 0
            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()

                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runDFS = DepthFirstSearch(self.startCity, self.goalCity, self.cityLocations,
                                          self.mappingCitiesToConnectedNeighbours)
                runDFS.depthFirstSearchIterative()
                numberNodesCreated = runDFS.numberOfNodesCreated
                numberNodesVisited = runDFS.numberOfCitiesVisited
                solutionFound = runDFS.solutionFound
                solutionPath = runDFS.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumAverageNodeInMemory += runDFS.maxNumberOfNodesInMemory
                sumLengthOfSolution += self.calcLengthOfSolution(runDFS.searchSolution)


            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches /100
            averageNodesInMemory = sumAverageNodeInMemory / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Nodes in Memory: ', averageNodesInMemory)
            print('Average Number Of Cities visited In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)
            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
        elif arg == 'BFS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumAverageNodeInMemory = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runBFS = BreadthFirstSearch(self.startCity, self.goalCity, self.cityLocations,
                                          self.mappingCitiesToConnectedNeighbours)
                runBFS.breadthFirstSearch()
                numberNodesCreated = runBFS.numberOfNodesCreated
                numberNodesVisited = runBFS.numberOfNodesVisited
                solutionFound = runBFS.solutionFound
                solutionPath = runBFS.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumAverageNodeInMemory += runBFS.maxNumberOfNodesInMemory
                sumLengthOfSolution += self.calcLengthOfSolution(runBFS.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches /100
            averageNodesInMemory = sumAverageNodeInMemory / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Nodes in Memory: ', averageNodesInMemory)
            print('Average Number of Cities visited in Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)

    def getEuclideanDistance(self, fromCity, toCity):
        x = (fromCity[0] - toCity[0]) ** 2
        y = (fromCity[1] - toCity[1]) ** 2
        z = x + y
        return math.sqrt(z)

    def calcLengthOfSolution(self, searchSolution):
        toCity = False
        sumLengthOfSolution = 0
        for fromCity in searchSolution:
            if toCity:
                fromCityLocation = self.cityLocations[fromCity]
                toCityLocation = self.cityLocations[toCity]
                sumLengthOfSolution += self.getEuclideanDistance(fromCityLocation, toCityLocation)
            toCity = fromCity
        return sumLengthOfSolution
