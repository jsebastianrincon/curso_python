#Asignacion de variables
x = 5
y = 3
#Operacion de variables
z = x + y
#Impresion de las variables
print (x)
print (y)
print (z)

#La variable w obtiene la misma direccion de Z

w = z
print(w)

#Muestra la direccion de la variable w en memoria pero solo funciona en la consola de Python
id(x)