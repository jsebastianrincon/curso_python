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
concatenacion = 'Hola' + ' Mundo'
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

#Reemplazando Cadenas

nueva_cadena = concatenacion.replace('Hola ','Adios ')
print(f'Nueva Cadena Reemplazada:{nueva_cadena}')

#Separar subcadenas

nueva_cadena = 'Hola Mundo'
lista = nueva_cadena.split() #Separa por defecto cada elemento con un espacio en blanco
print(lista)

datos = 'Sebastian,27,Colombia'
listab = datos.split(',')
print(listab)

#Multiplicacion de cadenas

print("********* MULTIPLICACION DE CADENAS *******")
texto = 'Hola'
veces = 2
resultado = texto * veces
print(resultado)