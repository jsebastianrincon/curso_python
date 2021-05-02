# Un diccionario esta compuesto por una llave,valor(key,value)

diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Mangament System"
}

print(diccionario)

# Largo de diccionario
print(len(diccionario))

# Acceder a un elemento
print(diccionario["IDE"])

# Acceder a un elemento metodo 2
print(diccionario.get("IDE"))

# Modificar un valor
diccionario["IDE"] = "Integrated development enviroment"
print(diccionario)

# Iteraciones del diccionarios
for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])

for valor in diccionario.values():
    print(valor)

# Comprobacion de valores
print("IDE" in diccionario)
print("Valor" in diccionario)

# Adicion de nuevos terminos
diccionario["PK"] = "Primary Key"
print(diccionario)

# Remover elementos
diccionario.pop("DBMS")
print(diccionario)

# Limpiar
# diccionario.clear()


# eliminar variables
#del diccionario
