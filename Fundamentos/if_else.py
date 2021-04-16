condicion = 10

if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion No Catalogada")


Numero = int(input("Ingrese un numero entre 1 y 3: "))
if(Numero == 1):
    numeroTexto = "Numero Uno"
elif (Numero == 2):
    numeroTexto = "Numero Dos"
elif (Numero == 3):
    numeroTexto = "Numero Tres"
else:
    numeroTexto = "Fuera de Rango"

print("Numero Proporcionado", numeroTexto)
