def saludar(nombre: str) ->str:
    saludo = "Hola desde Python " + str(nombre)
    return saludo

nombre = input("Deme su nombre: ")
print(saludar(nombre))