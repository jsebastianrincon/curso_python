from empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
# Envio de referencias para el uso de objetos

    def __str__(self):
        return super().__str__() + ",Departamento " + self.departamento
