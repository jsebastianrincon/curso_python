# Las clases inician con mayuscula si son varias palabras todas inician con mayuscula
class Persona:

    # Definicion de atributos del metodo
    def __init__(self, nombre, edad):
        # Asignacion de parametros a atributos
        self.nombre = nombre
        self.edad = edad


# Asignar datos a los valores
Persona.nombre = "Juan"
Persona.edad = 24

# Acceder a los valores
print(Persona.nombre)
print(Persona.edad)
print(id(Persona))

# Creacion de un objeto
persona = Persona("Sebastian", 24)
print(persona.nombre)
print(persona.edad)

# Muestra de direcciones en memoria
print(id(persona))

# Creacion de objeto nuevo
persona2 = Persona("Armando", 16)
print(persona2.nombre)
print(persona2.edad)

# Muestra de direcciones en memoria
print(id(persona2))
