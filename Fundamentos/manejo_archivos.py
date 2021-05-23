try:
    archivo = open("prueba.txt", "w")
    archivo.write("Agregamos Texto \n")
    archivo.write("Por Juan Sebastian Rincon")
except Exception as e:
    print(e)
finally:
    archivo.close()
    # Despues de close no se puede añadir nada sobre el archivo
    #archivo.write("Nueva Linea")
