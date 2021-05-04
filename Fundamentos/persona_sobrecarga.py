class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

# Sobreescribir metodo de la clase padre object

    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre

    def __sub__(self, otro):
        return "Operacion Invalida "


p1 = Persona("Juan")
p2 = Persona("Sebastian")

# Concatenacion desde el metodo de la clase padre
print(p1 + p2)

print(p1 - p2)
