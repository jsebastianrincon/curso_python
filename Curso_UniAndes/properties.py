class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad_nueva):
        if edad_nueva > 0 and edad_nueva < 110:
            self._edad = edad_nueva

    @property
    def nombre(self):
            return self.nombre

persona = Persona("Felipe", 25)
print(persona._edad)
persona.edad = 30
print(persona._edad)