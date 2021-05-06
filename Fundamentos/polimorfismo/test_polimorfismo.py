from empleado import Empleado
from gerente import Gerente

# Los metodos deben ser definidos antes de utilizarlo

# La variable puede apuntar a cualquier tipo

# Una variable puede ejecutar un metodo de x clase o de otra sin problema alguno


def imprimir_detalles(objeto):

    print(objeto)
    print(type(objeto), end="\n\n")
    # Determina si la variable es instancia
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Juan", 2000000)
imprimir_detalles(empleado)

empleado = Gerente("Sebastian", 6000000, "Sistemas")
imprimir_detalles(empleado)
