# Colecciones set no tienen orden y los datos son unicos e inmodifiicables,y no tienen indices

planetas = {"Mercurio", "Venus", "Tierra"}
print(planetas)

# Longitud
print(len(planetas))

# Existencia de un objeto
print("Tierra" in planetas)

# Agregar elementos
planetas.add("Marte")
print(planetas)

# Eliminar elementos
planetas.remove("Venus")
print(planetas)

# Eliminar elementos
planetas.discard("Marte")
print(planetas)
planetas.discard("Pluton")
print(planetas)

# Limpiar Set
planetas.clear()
print(planetas)

# Eliminar Set
del planetas
print(planetas)
