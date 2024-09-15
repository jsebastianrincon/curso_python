# Inmutabilidad

cadena1 = 'Hola Mundo'

#cadena1[0] = 'h'

#print(cadena1)

#Las cadenas son inmutables no se pueden modificar sus caracteres
cadena2 = cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)