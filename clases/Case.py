from clases.Tablero import *
from clases.Barco import *
from Conventions import *
from juego import CASO_NO_JUGADO, CASO_AGUA, CASO_TOCADO
from clases.Barco import Barco

barcos = Barco.get_instances()


instances = {}
jugadas = set()

class Casilla:
    def __init__(self, x, y):
        # Adición de las coordenadas
        self.x = x
        self.y = y
        # Queremos poder acceder a una casilla a partir de sus coordenadas
        instances[x, y] = self

        # Generación del nombre de la casilla
        self.nombre = f"{chr(x+65)}{y+1}"  # generación del nombre sin llamar al método _generar_nombre
        # Queremos poder acceder a una casilla a partir de su nombre
        instances[self.nombre] = self

        # Evolución de la casilla
        self.jugada = False
        self.barco = None  # No toca a un barco de momento.

    def jugar(self):
        """Describe qué pasa cuando jugamos una casilla"""
        self.jugada = True
        jugadas.add(self)

        if self.barco is not None:
            if len(self.barco.casillas - jugadas) == 0:
                print("Hundido !!")
            else:
                print("Tocado !")
        else:
            print("Agua !")

    @classmethod
    def generar_casillas(cls):
        for x, y in product(range(tablero_num_lineas),
                            range(tablero_num_columnas)):
            cls(x, y)

    def __str__(self):
        """Sobrecarga del método de transformación en cadena"""
        if not self.jugada:
            return CASO_NO_JUGADO
        elif self.barco is None:
            return CASO_AGUA
        return CASO_TOCADO

