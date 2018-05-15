from CityMapRepresentation import CityMapRepresentation
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from IterativeDeepeningSearch import IterativeDeepeningSearch
from GreedyBestFirst import GreedyBestFirst
from AStar import AStar
import sys
from PrintMap import PrintMap
import time


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
            print('Start city is: ')
            print(self.startCity)
            print('Goal city is: ')
            print(self.goalCity)
            runDFS = DepthFirstSearch( self.startCity, self.goalCity, self.cityLocations,
                                       self.mappingCitiesToConnectedNeighbours)
            runDFS.depthFirstSearch()
            self.allActionsTaken = runDFS.allActionsTaken
            self.searchSolution = runDFS.searchSolution
            print('Number of Nodes Visited: ', runDFS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runDFS.numberOfNodesCreated)
            print('Solution length: ', len(runDFS.searchSolution))
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
            print('Number of Nodes Visited: ', runIDS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runIDS.numberOfNodesCreated)
            print('Solution length: ', len(runIDS.searchSolution))
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
            print('Number of Nodes Visited: ', runBFS.numberOfNodesVisited)
            print('Number of Nodes Created: ', runBFS.numberOfNodesCreated)
            print('Solution length: ', len(runBFS.searchSolution))
        elif sys.argv[1] == 'IDS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumSolutionLength = 0
            start_time = time.time()
            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                runIDS = IterativeDeepeningSearch(self.startCity, self.goalCity, self.cityLocations,
                                                  self.mappingCitiesToConnectedNeighbours)
                runIDS.iterativeDS()
                numberNodesCreated = runIDS.numberOfNodesCreated
                numberNodesVisited = runIDS.numberOfCitiesVisited
                solutionFound = runIDS.solutionFound
                solutionPath = runIDS.searchSolution
                solutionLength = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumSolutionLength += solutionLength
            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveSolutonLength = sumSolutionLength / 100
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Solution Length: ', aveSolutonLength)
            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ' , elapsed_time)
        elif sys.argv[1] == 'DFS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumSolutionLength = 0
            start_time = time.time()
            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                runDFS = DepthFirstSearch(self.startCity, self.goalCity, self.cityLocations,
                                          self.mappingCitiesToConnectedNeighbours)
                runDFS.depthFirstSearch()
                numberNodesCreated = runDFS.numberOfNodesCreated
                numberNodesVisited = runDFS.numberOfCitiesVisited
                solutionFound = runDFS.solutionFound
                solutionPath = runDFS.searchSolution
                solutionLength = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumSolutionLength += solutionLength

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveSolutonLength = sumSolutionLength / 100
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Solution Length: ', aveSolutonLength)
            print('Number problems Solved: ', numberProbsSolved)
            print('Total time taken: ', elapsed_time)
        elif sys.argv[1] == 'BFS100':
            numberProbsSolved = 0
            sumNodesCreated = 0
            sumNodesVisited = 0
            sumSolutionLength = 0
            start_time = time.time()
            for i in range(0, 99):
                newMap = CityMapRepresentation()
                newMap.generateCityLocations()
                self.startCity = newMap.startCity
                self.goalCity = newMap.goalCity
                self.cityLocations = newMap.cityLocations
                self.mappingCitiesToConnectedNeighbours = newMap.mappingCitiesToConnectedNeighbours
                runBFS = BreadthFirstSearch(self.startCity, self.goalCity, self.cityLocations,
                                          self.mappingCitiesToConnectedNeighbours)
                runBFS.breadthFirstSearch()
                numberNodesCreated = runBFS.numberOfNodesCreated
                numberNodesVisited = runBFS.numberOfNodesVisited
                solutionFound = runBFS.solutionFound
                solutionPath = runBFS.searchSolution
                solutionLength = len(solutionPath)
                if solutionFound:
                    numberProbsSolved += 1
                sumNodesCreated += numberNodesCreated
                sumNodesVisited += numberNodesVisited
                sumSolutionLength += solutionLength

            elapsed_time = time.time() - start_time
            aveNodesCreated = sumNodesCreated / 100
            aveNodesVisited = sumNodesVisited / 100
            aveSolutonLength = sumSolutionLength / 100
            print('Average Nodes Visited: ', aveNodesVisited)
            print('Average Nodes Created: ', aveNodesCreated)
            print('Average Solution Length: ', aveSolutonLength)
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
            runGBS = GreedyBestFirst(self.startCity, self.goalCity, self.cityLocations,
                                              self.mappingCitiesToConnectedNeighbours)
            print('GBF Euclidean')
            runGBS.greedyBestFirstSearchEuclidean()
            self.allActionsTaken = runGBS.allActionsTaken
            self.searchSolution = runGBS.searchSolution
            print('Number of Nodes Visited: ', runGBS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runGBS.numberOfNodesCreated)
            print('Solution length: ', len(runGBS.searchSolution))
            print('GBF Manhattan')
            runGBS.greedyBestFirstSearchManhattan()
            self.allActionsTaken = runGBS.allActionsTaken
            self.searchSolution = runGBS.searchSolution
            print('Number of Nodes Visited: ', runGBS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runGBS.numberOfNodesCreated)
            print('Solution length: ', len(runGBS.searchSolution))
            print('GBF h(n) = 0')
            runGBS.greedyBestFirstSearchNoHeuristic()
            self.allActionsTaken = runGBS.allActionsTaken
            self.searchSolution = runGBS.searchSolution
            print('Number of Nodes Visited: ', runGBS.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runGBS.numberOfNodesCreated)
            print('Solution length: ', len(runGBS.searchSolution))
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
            print('A* Euclidean')
            runAStar.AStarEuclidean()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Solution length: ', len(runAStar.searchSolution))
            print('A* Manhattan')
            runAStar.AStarManhattan()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Solution length: ', len(runAStar.searchSolution))
            print('A* h(n) = 0')
            runAStar.AStarNoHeuristic()
            self.allActionsTaken = runAStar.allActionsTaken
            self.searchSolution = runAStar.searchSolution
            print('Number of Nodes Visited: ', runAStar.numberOfCitiesVisited)
            print('Number of Nodes Created: ', runAStar.numberOfNodesCreated)
            print('Solution length: ', len(runAStar.searchSolution))

        if len(sys.argv) < 3:
            print('Not printing map')
        elif sys.argv[2] == 'print':
            printMap = PrintMap(self.mappingCitiesToConnectedNeighbours, self.startCity, self.goalCity,
                                     self.cityLocations, self.searchSolution, self.allActionsTaken)
            printMap.mainloop()


runProg  = introAi()

