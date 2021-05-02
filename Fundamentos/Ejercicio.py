# Clase padre

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

# Acceso a atributos de clase

    def __str__(self):
        return "Color:" + self.color + ", Numero de ruedas:" + str(self.ruedas)

# Clase coche hereda de vehiculo (Hija)


class Carro(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        # super() accede a las clases padre
        super().__init__(color, ruedas)
        self.velocidad = velocidad

        def __str__(self):
            return super().__str__() + ", Velocidad: " + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        # super() accede a las clases padre
        super().__init__(color, ruedas)
        self.tipo = tipo

        def __str__(self):
            return super().__str__() + ", Tipo: " + str(self.tipo)

# Objeto clase padre


vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)

carro = Carro("Azul", 4, 300)
print(carro)

bicicleta = Bicicleta("Negra", 2, "Carreras")
print(bicicleta)
