# Cadenas

cadena1 = 'Hola Mundo'
cadena1 = 'Adios'
cadena2 = "Python es genial"
cadena3 = '''Este es un ejemplo 
            de multiples lineas
                en una cadena'''

print(cadena1)
print(cadena2)
print(cadena3)


#Concatenacion de cadenas
cadenaA = 'Hola'
cadenaB = 'Mundo'
concatenacion = 'Hola' + 'Mundo'
concatenacionB = cadenaA + cadenaB
concatenacionC = cadenaA + ' ' + cadenaB
print(concatenacion)
print(concatenacionB)
print(concatenacionC)

#Utilizando Join

concatenacionD = ''.join([cadenaA,' ',cadenaB])
print(concatenacionD)

nombre  = 'Juan'
edad = 27
mensaje = f'Hola, me llamo {nombre} y tengo {edad}'
print(mensaje)

#Usando format

mensaje = 'Hola, me llamo {} y tengo {}'.format(nombre, edad)
print(mensaje)

