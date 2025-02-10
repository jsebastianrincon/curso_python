# Conversion de datos

# Cadena a Numero

numero_cadena = '10'
numero_entero = int(numero_cadena)

print (f'Valor numerico en cadena:{numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

# Convertir de cadena a float
numero_cadena = 3.14
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante:{numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a Cadena:{numero_cadena}')

#Convertir a booleano
#Tipo bool es falos en los siguientes casos
#Regresa verdadero, si el valor es distinto de 0, si es distinto de cadena vacia
#y tambien si es disntinto de None

numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor Booleano de 0:{booleano}')


numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor Booleano de 5:{booleano}')


cadena = ''
booleano = bool(cadena)
print(f'Valor Booleano de cadena vacia:{booleano}')

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor Booleano de cadena NO vacia:{booleano}')

cadena = ''
booleano = bool(cadena)
print(f'Valor booleano de cadena vacia:{booleano}')