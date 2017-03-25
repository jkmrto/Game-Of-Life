from __future__ import print_function
import logging
import copy

logger = logging.getLogger("MainLogger")

class grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.table = []
        self.adj_live_cell_grid = None
        self.previous_table = []

    def generateEmptyGrid(self):
        self.table = []

        for i in range(0, self.rows):
            self.table.append(["-"] * self.columns)

    def printGrid(self):
        print("Column\t", end="")

        for j in range(1, self.columns + 1):
            print("{}\t".format(j), end="")
        print("")

        for i in range(0, self.rows):
            print("Row\t {}\t".format(i + 1), end='')
            for j in range(0, self.columns):
                print("{}\t".format(self.table[i][j]), end='')
            print("")


    def getAdj(self):
        self.adj_live_cell_grid = copy.deepcopy(self.table)  # Inicializacion dimensional de la lista

        for row_pos in range(0, self.rows):
            for column_pos in range(0, self.columns):
                logger.debug(
                    "Cell which his adjacent will we evaluated -> row:{0}, column:{1}".format(row_pos, column_pos))
                self.adj_live_cell_grid[row_pos][column_pos] = self.getAdjCell(row_pos, column_pos)

    def getAdjCell(self, row_pos, column_pos):
        counter = 0

        for mini_row_pos in range(row_pos - 1, row_pos + 2):
            for mini_column_pos in range(column_pos - 1, column_pos + 2):
                logger.debug("Posicion: {0},{1}".format(mini_row_pos, mini_column_pos))
                if (mini_row_pos >= 0 and mini_row_pos < self.rows) and \
                        (mini_column_pos >= 0 and mini_column_pos < self.columns):
                    logger.debug("Dentro del tablero")
                    if (not ((mini_row_pos == row_pos) and (mini_column_pos == column_pos))):
                        logger.debug(
                            "No es el centro, contiene {}".format(self.table[mini_row_pos][mini_column_pos]))
                        if self.table[mini_row_pos][mini_column_pos] == '*':
                            logger.debug(self.table[mini_row_pos][mini_column_pos])
                            counter = counter + 1
                        else:
                            counter = counter
                    else:
                        logger.debug("Es el centro")
                        counter = counter
                else:
                    counter = counter
        logger.debug("{0} cell alive adj to position ->  row:{1}, column -> {1}".
                     format(counter, row_pos, column_pos))

        return counter

    def print_adj(self):
        print("Amount of next cells alives")
        for row_pos in range(0, self.rows):
            for column_pos in range(0, self.columns):
                print("{}\t".format(self.adj_live_cell_grid[row_pos][column_pos]), end='')
            print('')

    def placeLiveCellsInGrid(self, cellsLivePosition):
        for cell_id in cellsLivePosition:
#            print("{0},{1},{2}".format(cell_id, cell_id / self.columns, cell_id % self.columns))

            self.table[int(cell_id / self.columns)][cell_id % self.columns] = '*'

    def isEmptyGrid(self):
        return (len([symbol for row in self.table for symbol in row if symbol == '*']) == 0)

    def update(self):
        self.previous_previous_table = self.previous_table
        self.previous_table = copy.deepcopy(self.table)
        for row_pos in range(0, self.rows):
            for column_pos in range(0, self.columns):
                self.updateCell(row_pos, column_pos)

    def updateCell(self, row_pos, column_pos):

        if self.table[row_pos][column_pos] == '*':
            if (self.adj_live_cell_grid[row_pos][column_pos] == 2) or (self.adj_live_cell_grid[row_pos][column_pos] == 3):
                self.table[row_pos][column_pos] = '*'
            else:
                self.table[row_pos][column_pos] = '-'
        else:
            if self.adj_live_cell_grid[row_pos][column_pos] == 3:
                self.table[row_pos][column_pos] = '*'

    def isAlreadyStillLife(self):
        return self.table == self.previous_table

    def nextStep(self):
        self.getAdj()
        self.update()