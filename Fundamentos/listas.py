# Una lista es una coleccin de elementos
# Las cadenas se pueden con comilla simple o doble no importa

nombres = ["Juan", "Sebastian", "Alejandra", "Rocky"]
print(nombres)

# Longiutd de lista
print(len(nombres))

# Elemento 0
print(nombres[0])
print(nombres[1])

# Navegacion inversa
print(nombres[-1])
print(nombres[-2])

# Imprimir por rangos
# Excluye el 2
print(nombres[0:2])

# Imprimir los elementos de inicio hasta el indice solicitado
# Excluye el 3
print(nombres[:3])

# Imprimir elementos hasta el final del indice solicitado desde el indice 1
print(nombres[1:])

# Cambio de elementos de lista
nombres[3] = "Armando"
print(nombres)

# Iteracion de listas
for nombre in nombres:
    print(nombre)

# Existencia de elementos en la lista
if "Armando" in nombres:
    print("Armando si existe en la lista")
else:
    print("No existe")

# Adicion de nuevos elementos
# Agrega como ultimo elemento en la lista
nombres.append("Eder")
print(nombres)
# Insertar elemento donde se indica
nombres.insert(1, "Juana")
print(nombres)

# Remover elementos donde se indica
nombres.remove("Juana")
print(nombres)

# Remover ultimo elemento de lista
nombres.pop()
print(nombres)

# Remover donde se indica
del nombres[1]
print(nombres)

# Limpiar elementos de lista
nombres.clear()
print(nombres)

# Eliminar por completo lista
del nombres
print(nombres)
