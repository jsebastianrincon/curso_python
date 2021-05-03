# Las clases cargadas no cargan los objetos,esto hace que el contexto estatico
# No accedan a variables de instancia pero si a las demas funciones estaticas

# Metodos de clases

class MiClase:

    variable_clase = "Variable Clase"

    def __init__(self):
        self.variable_instancia = "Variable de instancia"

    # Decorador que permite agregar funcionalidades a un metodo
    # No se reciben parametro y no se puede acceder a variables
    @staticmethod
    # Los metodos no reciben parametros
    def metodo_estatico():
        # Self solo funcina para objetos no en metodos
        print("Metodo Estatico")
        print(MiClase.variable_clase)
        # Los metodos estaticos no se puede acceder a variables de instancia
        # print(MiClase.variable_instancia)

    # Metodo de clase reciben parametros del contexto estatico

    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase:" + str(cls))
        print(cls.variable_clase)
        # No se puede acceder a una instancia desde un contexto estatico
        # print(cls.variable_instancia)

    def metodo_instancia(self):
        self.metodo_clase
        self.metodo_estatico
        print(self.variable_clase)
        print(self.variable_instancia)


MiClase.metodo_estatico()
MiClase.metodo_clase()

print()
objeto1 = MiClase()
objeto1.metodo_instancia()
