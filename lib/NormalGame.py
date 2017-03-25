from lib.GameOfLife import game
import os
import random


class NormalGame(game):
    def __init__(self, filas, columnas, NumberOfCellsAlive):
        game.__init__(self, filas, columnas)
        self.gridPanel = self.generateInitialGrid()
        self.placeLiveCellsRandomly(NumberOfCellsAlive)

    def placeLiveCellsRandomly(self, cellsLiveRequired):
        cellsLivePosition = self.generateRandomPosition(cellsLiveRequired)
        self.gridPanel.placeLiveCellsInGrid(cellsLivePosition)

    def execute(self):

        while not self.isAlreadyStillLife():
            print("Presionar cualquier tecla para continuear")
            os.system("pause")

            self.nextStep()
            self.printGrid()

        if self.isEmptyGrid():
            print("El tablero inicial generado no contiene 'Still Life Pattern'")
        else:
            print("El 'Still Life Pattern' encontrado es:")
            self.printGrid()


    def generateRandomPosition(self, cellsLiveRequired):
        cellsLivePosition = []
        all_cells_placed = False

        while not all_cells_placed:
            aux_cell_identifier = random.randrange(self.rows * self.columns)
            if aux_cell_identifier not in cellsLivePosition:
                cellsLivePosition.append(aux_cell_identifier)
                if len(cellsLivePosition) == cellsLiveRequired:
                    all_cells_placed = True

        return cellsLivePosition

    def printGrid(self):
        self.gridPanel.printGrid()

    def generateEmptyGrid(self):
        self.gridPanel.generateEmptyGrid()

    def nextStep(self):
        self.gridPanel.nextStep()

    def isAlreadyStillLife(self):
        return self.gridPanel.isAlreadyStillLife()

    def isEmptyGrid(self):
        return self.gridPanel.isEmptyGrid()