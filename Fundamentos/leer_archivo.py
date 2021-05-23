# Llamado del texto
#archivo = open("C:\\Users\\Acer\\Documents\\Cursos\\Python\\prueba.txt", "r")
archivo = open("prueba.txt", "r")

# Imprime el contenido del archivo
# print(archivo.read())

# Lectura de algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# Lectura de lineas completas
# print(archivo.readline())
# print(archivo.readline())

# Iteracion
# for linea in archivo:
#    print(linea)

# Lectura de lineas
# print(archivo.readlines())

# Acceder a una linea de la lista
# print(archivo.readlines()[2])

# Abrir nuevo archivo con nueva informacion
# Con a se anexa nueva informacion al archivo

#archivo2 = open("copia.txt", "a")

archivo2 = open("copia.txt", "w")

# Escribe lo de otro archivo
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
