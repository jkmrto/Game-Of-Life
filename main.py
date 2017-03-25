import sys
import os
from lib.NormalGame import NormalGame
from lib.SearchingStillLifeGame import SearchingStillLiveGame
from lib.AuxiliarFunctions import init_logging_system
from lib.AuxiliarFunctions import introducir_entero_y_comprobar

def EspecificarParametros():
    print("Introducir las dimensiones del tablero del juego:")
    columnas = introducir_entero_y_comprobar("columnas")
    filas = introducir_entero_y_comprobar("filas")
    NumeroceldasVivas = introducir_entero_y_comprobar("numero de celdas vivas al inicio")
    return filas, columnas, NumeroceldasVivas

def DefaultGame():

    filas, columnas, NumeroceldasVivas = EspecificarParametros()

    juego = NormalGame(filas, columnas, NumeroceldasVivas)
    print("El tablero inicial generado es:")
    juego.printGrid()

    juego.execute()


def SearchingAllStillLifePatternGame():
    filas, columnas, NumeroceldasVivas = EspecificarParametros()
    juego = SearchingStillLiveGame(filas, columnas, NumeroceldasVivas)
    juego.execute_till_found_pattern()


def SearchingStillLifeOneStep():
    filas, columnas, NumeroceldasVivas = EspecificarParametros()
    juego = SearchingStillLiveGame(filas, columnas, NumeroceldasVivas)
    juego.execute_one_step()


def seleccionarJuegoImpresionPorPantalla():

    print("Seleccionar  el juego:")
    print("\t 0) Salir del juego")
    print("\t 1) Obtener el 'Still Life Patterns' de un tablero creado aleatoriamente")
    print("\t 2) Encontrar  los 'Still Life Pattern' generados en un solo paso")
    print("\t 3) Encontrar los 'Still Life Pattern' generados en múltiples pasos")
    caracter_insertado = input("Seleccionar '0', '1', '2', 3: ")

    return caracter_insertado


def evaluarOpcionEscogidaYlanzarJuego():
    if caracter_insertado == '1':
        DefaultGame()
    elif caracter_insertado == '2':
        SearchingStillLifeOneStep()
    elif caracter_insertado == '3':
        SearchingAllStillLifePatternGame()
    elif caracter_insertado == '0':
        sys.exit(0)
    else:
        print("El caracter {} introducido no es valido".format(caracter_insertado))

if __name__ == "__main__":
    juego_valido = False
    init_logging_system()

    while True:
            caracter_insertado = seleccionarJuegoImpresionPorPantalla()
            juego_valido = evaluarOpcionEscogidaYlanzarJuego()

