# Clase padre

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Acceso a atributos de clase

    def __str__(self):
        return "Nombre:" + self.nombre + ", Edad:" + str(self.edad)

# Clase empleado hereda de persona (Hija)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # super() accede a las clases padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo

        def __str__(self):
            return super().__str__() + ", sueldo: " + str(self.sueldo)

# Objeto clase padre


persona = Persona("Sebastian", 24)
print(persona)

empleado = Empleado("Armando", 30, 500.00)
print(empleado)

empleado.nombre = "Juan"
empleado.sueldo = 1000.00
empleado.edad = 24
print(empleado)
