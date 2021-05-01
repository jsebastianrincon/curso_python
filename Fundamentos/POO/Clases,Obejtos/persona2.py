# Las clases inician con mayuscula si son varias palabras todas inician con mayuscula

class Persona:

    # Definicion de atributos del metodo
    # * ---> valor opcional
    def __init__(this, n, e, *v, **d):
        # Asignacion de parametros a atributos con apuntadores
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(this):
        print("Nombre", this.nombre)
        print("Edad", this.edad)
        print("Valores(Tupla):", this.valores)
        print("Diccionario", this.diccionario)


# Clases con implementacion de tuplas
# Asignar datos a los valores
p1 = Persona("Juan", 24)
p1.desplegar()
print()

p2 = Persona("Sebastian", 24, 2, 4, 5)
p2.desplegar()
print()

p3 = Persona("Maria", 22, 2, 4, 5, m="Manzana", p="Pera", N="Naranja")
p3.desplegar()
