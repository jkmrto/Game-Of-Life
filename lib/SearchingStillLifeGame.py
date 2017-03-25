from lib.GameOfLife import game
from lib.Combinations import combinations
from lib.GridPanel import grid
from lib.AuxiliarFunctions import printAnyGrid

class SearchingStillLiveGame(game):
    def __init__(self, filas, columnas, NumberOfAlivesCell):
        game.__init__(self, filas, columnas)
        self.allGrid = []
        self.limit_number_nextSteps = 10 * self.rows * self.columns
        self.stillLifePatternsFound = []
        self.stillLifePatternsNotRepeated = []
        self.completeInitialGridsWithAllLiveCellsCombinationPosible(NumberOfAlivesCell)


    def execute_one_step(self):

        for gridSelected in self.allGrid:
            gridSelected.nextStep()
            if not gridSelected.isAlreadyStillLife():
                gridSelected.generateEmptyGrid()

        self.selectStillLifePatternFromAllGridGenerated()

        print('Still Life Pattern Encontrados')
        self.filterNotRepeatedStillLifePattern()
        self.printNotRepeatedStillLifePattern()


    def execute_till_found_pattern(self):

        for gridSelected in self.allGrid:
            #print("Analizando el grid:")
            #gridSelected.printGrid()
            counter = 0
            while (not gridSelected.isAlreadyStillLife())  and (counter < self.limit_number_nextSteps):
                gridSelected.nextStep()
                counter += 1

            if counter == (self.limit_number_nextSteps):
                gridSelected.generateEmptyGrid()

            # print('Resultado:')
            # gridSelected.printGrid()

        # print("Still Life Pattern Encontrados de cada Grid")
        self.selectStillLifePatternFromAllGridGenerated()
        #self.printStillLifePatternFound()

        print('Still Life Pattern Encontrados')
        self.filterNotRepeatedStillLifePattern()
        self.printNotRepeatedStillLifePattern()

    def completeInitialGridsWithAllLiveCellsCombinationPosible(self, NumberOfAlivesCell):

        allCombinationsPosible = combinations(range(self.columns * self.rows), NumberOfAlivesCell)

        for cellsLivePosition in allCombinationsPosible:
             aux_grid = self.generateInitialGrid()

             aux_grid.placeLiveCellsInGrid(cellsLivePosition)
             self.allGrid.append(aux_grid)

    def printAllGrid(self):
        for selected_grid in self.allGrid:
            selected_grid.printGrid()

    def selectStillLifePatternFromAllGridGenerated(self):
        for gridSelected in self.allGrid:
           #2
           #  gridSelected.printGrid()
            if not gridSelected.isEmptyGrid():
                self.stillLifePatternsFound.append(gridSelected.table)

    def printStillLifePatternFound(self):

        for StillLifePatternSelected in self.stillLifePatternsFound:
            printAnyGrid(StillLifePatternSelected, self.rows, self.columns)

    def filterNotRepeatedStillLifePattern(self):

        for stillLifePartternSelected in self.stillLifePatternsFound:
            if not stillLifePartternSelected  in self.stillLifePatternsNotRepeated:
                self.stillLifePatternsNotRepeated.append(stillLifePartternSelected)

    def printNotRepeatedStillLifePattern(self):
        for StillLifePatternSelected in self.stillLifePatternsNotRepeated:
            printAnyGrid(StillLifePatternSelected, self.rows, self.columns)


