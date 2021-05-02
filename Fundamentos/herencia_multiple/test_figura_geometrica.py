from cuadrado import Cuadrado
from figura_geometrica import FiguraGeometrica

#figuraGeometrica = figuraGeometrica()
cuadrado = Cuadrado(4, "Azul")
print(cuadrado.area())
print(cuadrado.color)

# Muestra el orden de ejecucion de las clases
print(Cuadrado.mro())
