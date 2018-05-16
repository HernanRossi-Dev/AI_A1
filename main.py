from CityMapRepresentation import CityMapRepresentation
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from IterativeDeepeningSearch import IterativeDeepeningSearch
from GreedyBestFirst import GreedyBestFirst
from AStar import AStar
import sys
from PrintMap import PrintMap
import time
import math


class introAi:
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
        self.run()

    def run(self):
        if len(sys.argv) < 2:
            print('Must supply type of search to perform')
            exit(0)
        if sys.argv[1] == 'DFS':
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
            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)
            print (' ')
        elif sys.argv[1] == 'IDS':
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
            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)

        elif sys.argv[1] == 'BFS':
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
            print ('Exact length of Solution: ', lengthOfSolutionExactDistance)

        elif sys.argv[1] == 'IDS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0
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
            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches /100
            aveLengthOfSolution = sumLengthOfSolution / 100
            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)
            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ' , elapsed_time)
        elif sys.argv[1] == 'DFS100':
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
        elif sys.argv[1] == 'BFS100':
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



        elif sys.argv[1] == 'GBF100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runGBF = GreedyBestFirst(self.startCity, self.goalCity, self.cityLocations,
                                            self.mappingCitiesToConnectedNeighbours)
                runGBF.greedyBestFirstSearchEuclidean()
                numberNodesCreated = runGBF.numberOfNodesCreated
                numberNodesVisited = runGBF.numberOfCitiesVisited
                solutionFound = runGBF.solutionFound
                solutionPath = runGBF.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumLengthOfSolution += self.calcLengthOfSolution(runGBF.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print ('Statistics for Greedy Best First using Euclidean Heuristic')
            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runGBF = GreedyBestFirst(self.startCity, self.goalCity, self.cityLocations,
                                            self.mappingCitiesToConnectedNeighbours)
                runGBF.greedyBestFirstSearchManhattan()
                numberNodesCreated = runGBF.numberOfNodesCreated
                numberNodesVisited = runGBF.numberOfCitiesVisited
                solutionFound = runGBF.solutionFound
                solutionPath = runGBF.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumLengthOfSolution += self.calcLengthOfSolution(runGBF.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print (' ')
            print ('Statistics for Greedy Best First using Manhattan Heuristic')

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runGBF = GreedyBestFirst(self.startCity, self.goalCity, self.cityLocations,
                                            self.mappingCitiesToConnectedNeighbours)
                runGBF.greedyBestFirstSearchNoHeuristic()
                numberNodesCreated = runGBF.numberOfNodesCreated
                numberNodesVisited = runGBF.numberOfCitiesVisited
                solutionFound = runGBF.solutionFound
                solutionPath = runGBF.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumLengthOfSolution += self.calcLengthOfSolution(runGBF.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print (' ')
            print ('Statistics for Greedy Best First using h(n)=0 Heuristic')

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
        elif sys.argv[1] == 'AStar100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runAStar = AStar(self.startCity, self.goalCity, self.cityLocations,
                                            self.mappingCitiesToConnectedNeighbours)
                runAStar.AStarEuclidean()
                numberNodesCreated = runAStar.numberOfNodesCreated
                numberNodesVisited = runAStar.numberOfCitiesVisited
                solutionFound = runAStar.solutionFound
                solutionPath = runAStar.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumLengthOfSolution += self.calcLengthOfSolution(runAStar.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print ('Statistics for A* using Euclidean Heuristic')
            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runAStar = AStar(self.startCity, self.goalCity, self.cityLocations,
                                            self.mappingCitiesToConnectedNeighbours)
                runAStar.AStarManhattan()
                numberNodesCreated = runAStar.numberOfNodesCreated
                numberNodesVisited = runAStar.numberOfCitiesVisited
                solutionFound = runAStar.solutionFound
                solutionPath = runAStar.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumLengthOfSolution += self.calcLengthOfSolution(runAStar.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print (' ')
            print ('Statistics for A* using Manhattan Heuristic')

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumNumberCitiesVisitedInSolution = 0
            start_time = time.time()
            sumAverageBranches = 0
            sumLengthOfSolution = 0

            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                sumAverageBranches += newMap.calcAverageBranches()

                runAStar = AStar(self.startCity, self.goalCity, self.cityLocations,
                                            self.mappingCitiesToConnectedNeighbours)
                runAStar.AStarNoHeuristic()
                numberNodesCreated = runAStar.numberOfNodesCreated
                numberNodesVisited = runAStar.numberOfCitiesVisited
                solutionFound = runAStar.solutionFound
                solutionPath = runAStar.searchSolution
                citiesInSolutionPath = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumNumberCitiesVisitedInSolution += citiesInSolutionPath
                sumLengthOfSolution += self.calcLengthOfSolution(runAStar.searchSolution)

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveNumCitiesInSolution = sumNumberCitiesVisitedInSolution / 100
            averageNumBranches = sumAverageBranches / 100
            aveLengthOfSolution = sumLengthOfSolution / 100

            print (' ')
            print ('Statistics for A* using h(n)=0 Heuristic')

            print('Average number of branches: ', averageNumBranches)
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Number Of Cities In Solution: ', aveNumCitiesInSolution)
            print('Average Length of Solution Distance: ', aveLengthOfSolution)

            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
        elif sys.argv[1] == 'GBF':
            print('Doing greedy best first')
            newMap = CityMapRepresentation()
            newMap.generateCityLocations()
            self.startCity = newMap.startCity
            self.goalCity = newMap.goalCity
            self.cityLocations = newMap.cityLocations
            self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
            runAStar = GreedyBestFirst(self.startCity, self.goalCity, self.cityLocations,
                                       self.mappingCitiesToConnectedNeighbours)
            print('GBF h(n) = 0')
            runAStar.greedyBestFirstSearchNoHeuristic()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Number of cities visited in Solution: ', len(runAStar.searchSolution))
            print('GBF Euclidean')
            runAStar.greedyBestFirstSearchEuclidean()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Number of cities visited in Solution: ', len(runAStar.searchSolution))
            print('GBF Manhattan')
            runAStar.greedyBestFirstSearchManhattan()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Number of cities visited in Solution: ', len(runAStar.searchSolution))
        elif sys.argv[1] == 'AStar':
            print('Doing A*')
            newMap = CityMapRepresentation()
            newMap.generateCityLocations()
            self.startCity = newMap.startCity
            self.goalCity = newMap.goalCity
            self.cityLocations = newMap.cityLocations
            self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
            runAStar = AStar(self.startCity, self.goalCity, self.cityLocations,
                                     self.mappingCitiesToConnectedNeighbours)
            print('A* h(n) = 0')
            runAStar.AStarNoHeuristic()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Number of cities in Solution: ', len(runAStar.searchSolution))
            print('A* Euclidean')
            runAStar.AStarEuclidean()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Number fo cities in Solution: ', len(runAStar.searchSolution))
            print('A* Manhattan')
            runAStar.AStarManhattan()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Number of cities in Solution: ', len(runAStar.searchSolution))


        if len(sys.argv) < 3:
            print('Not printing map')
        elif sys.argv[2] == 'print':
            printMap = PrintMap(self.mappingCitiesToConnectedNeighbours, self.startCity, self.goalCity,
                                     self.cityLocations, self.searchSolution, self.allActionsTaken)
            printMap.mainloop()

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

runProg  = introAi()

