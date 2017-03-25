from __future__ import print_function
from lib.GridPanel import grid
import logging
logger = logging.getLogger("MainLogger")


class game:
    def __init__(self, filas, columnas):
        self.rows = filas
        self.columns = columnas

    def generateInitialGrid(self):
        aux_grid = grid(self.rows, self.columns)
        aux_grid.generateEmptyGrid()
        return aux_grid




