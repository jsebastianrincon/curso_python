# Creacion de clase

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return self.base * self.altura


# Ingreso de datos para hacer el calculo
base = int(input("Ingrese base:"))
altura = int(input("Ingrese altura:"))

# Llamado de metodo para hacer calculo
rectangulo = Rectangulo(base, altura)

print(rectangulo.calcula_area())
