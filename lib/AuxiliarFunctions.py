from __future__ import print_function
import logging

def printAnyGrid(grid, rows, columns):
    print("Column\t", end="")

    for j in range(1, columns + 1):
        print("{}\t".format(j), end="")
    print("")

    for i in range(0, rows):
        print("Row\t {}\t".format(i + 1), end='')
        for j in range(0, columns):
            print("{}\t".format(grid[i][j]), end='')
        print("")

def introducir_entero_y_comprobar(string):
    correcto = False
    elemento = None

    while not correcto:
        elemento = input("Introduce el numero de {}: ".format(string))
        try:
            elemento = int(elemento)
            correcto = True
        except:
            print('El valor "{}" introducido no es valido'.format(elemento))

    return elemento


def init_logging_system():
    logger = logging.getLogger('MainLogger')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('Juego.log', 'w')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
