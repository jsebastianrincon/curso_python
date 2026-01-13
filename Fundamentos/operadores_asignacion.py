print("**** OPERADORES ****")


# Operador de asignacion
x = 3
print(x)

# Asignacion mas suma
# Equivale a sumarle 2 al valor de x
x += 2
print(x)

# Equivale a restarle 2 al valor de x
x -= 1
print(x)

# Equivale a multiplicar x*3
x *= 3
print(x)

#Equivale a dividir x/3
x/=2
print(x)

#Asignacion multiple
x, y, z = 5,'Hola',-9.15
print(f'Valor de x = {x},y = {y},z = {z}')

#Asignacion encadenada
a = b = c = 10
print(f'Valor de a = {a},b = {b},c = {c}')

#Intercambio de valores de una variable
x, y = 5, 10
print(f'Valores Iniciales x = {x}, y = {y}')

#Invirtiendo Valores
x , y = y , x 
print(f'Valores Invertidos x = {x}, y = {y}')

#Recibir multiples valores de la entrada del usuario
nombre, apellido = input("Ingrese nombres y apellidos separados por coma: ").split(',')
print(f'Nombre:{nombre.strip()},Apellido:{apellido.strip()}')
