# Crear metodos privados en clases

class Persona:
    def __init__(self, nombre, primer_ape, segundo_ape):
        # No privado
        self.nombre = nombre
        # Protegido
        self._primer_ape = primer_ape
        # Privado
        self.__segundo_ape = segundo_ape

    def metodo_publico(self):
        self.__metodo_privado()

     # Metodos Privados
    def __metodo_privado(self):
        print(self.nombre)
        print(self._primer_ape)
        print(self.__segundo_ape)

    def get_segundo_ape(self):
        return self.__segundo_ape

    def set_segundo_ape(self, segundo_ape):
        self.__segundo_ape = segundo_ape


p1 = Persona("Juan", "Rincon", "Calderon")
# p1.__metodo_privado()
p1.metodo_publico()

print(p1.nombre)
print(p1._primer_ape)
# print(p1.__segundo_ape())
print(p1.get_segundo_ape())
