#Metodos de cadena

cadena = ' Hola Mundo '
print(f'Cadena Original: {cadena}')

cadena_Mayuscula = cadena.upper()
print(cadena_Mayuscula) 

cadena_minuscula = cadena.lower()
print(cadena_minuscula)

cadena_sin_espacios = cadena.strip() #Cadena Sin Espacios en blanco
print(cadena_sin_espacios)
longitud = (len(cadena))
print(f'Longitud Cadena: {longitud}')


#Subcadenas

subcadena = cadena[0:4]
print(f'Subcadena: {subcadena}')

subcadena_mundo = cadena[6:11]
print(f'Subcadena Mundo: {subcadena_mundo}')

#Busqueda subcadenas
indice = cadena.find('Hola')
print(f'Busqueda Subcadena: {indice}')

#obtener mundo
indiceM = cadena.find('Mundo')
print(f'Busqueda Subcadena: {indiceM}')

indiceM = cadena.find('mundo')
print(f'Busqueda Subcadena: {indiceM}')

#Reemplazar
indiceR = cadena.replace('Mundo','A todos')
print(f'Cadena Original: {cadena}')
print(f'Nueva Cadena:{indiceR}')




