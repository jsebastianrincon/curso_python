#Asignacion de variables
x = 5
y = 3
#Operacion de variables
z = x + y
#Impresion de las variables
print ('Valores Iniciales: ')
print (x)
print (y)
print (z)

#La variable w obtiene la misma direccion de Z

w = z
print(w)

#Muestra la direccion de la variable w en memoria pero solo funciona en la consola de Python
id(x)

#Modificar variables
x = 10
y = 20
z = x + y

print ('Valores Finales: ')
print (x)
print (y)
print (z)


# En python el valor de las variables es dinamico

x = 'Diez'
y = 'Veinte'
z = 'Diez' + 'Veinte'

print ('Valores Dinamicos: ')
print (x)
print (y)
print (z)
