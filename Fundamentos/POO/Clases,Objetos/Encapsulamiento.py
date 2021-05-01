# Adicion de atributos a clases

class Persona:
    def __init__(self, nombre, edad):
        # Definicion de un atributo privado con doble raya piso
        self.__nombre = nombre
        self.__edad = edad

    # Get para lectura del atributo
    def get_nombre(self):
        return self.__nombre

    # Set para modificacion del atributo
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


# Asignacion de los atributos
p1 = Persona("Juan", 24)
print(p1.get_nombre())
print(p1.get_edad())

p1 = Persona("Sebastian", 23)
# Modificar edad

print(p1.get_nombre())
print(p1.get_edad())
