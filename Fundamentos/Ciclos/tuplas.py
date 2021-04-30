# Tuplas son listas que son ordenadas pero no se pueden modificar

frutas = ("Manzana", "Naranja", "Banano")
print(frutas)

# Longitud de tupla
print(len(frutas))

# Imprimir indice especifico
print(frutas[2])

# Navegacion Inversa
print(frutas[-2])

# Rango
print(frutas[0:2])  # Excluye el indice 2

# Modificar un valor
# Las tuplas no permiten adicion ni eliminacion de valores a menos que se convierta a una lista
#frutas[0] = "Manzanita"

# Conversion a lista
frutasLista = list(frutas)
frutasLista[1] = "Manzanita"
frutas = tuple(frutasLista)
print(frutas)

# Iteracion de tuplas
for fruta in frutas:
    print(fruta, end=" ")

# Elimina tupla completa
del frutas
