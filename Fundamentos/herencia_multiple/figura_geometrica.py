# Metodo abstracto
from abc import ABC, abstractmethod

# Clase abstracta


class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
# Metodo Abstracto

    @abstractmethod
    def area(self):
        pass
