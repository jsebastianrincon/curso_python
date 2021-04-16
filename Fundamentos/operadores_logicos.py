# Variables

#a = int(input("Ingrese un valor: "))
a = 3
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a <= valorMaximo)

# Condicional If

if(dentroRango):
    print("Esta en el rango")
else:
    print("Esta fuera del rango")

vacaciones = True
diaDescanso = False

if(vacaciones or diaDescanso):
    print("Se puede salir")
else:
    print("Hoy no se puede salir")

# Invirte el valor de la variables

# print(not(vacaciones))

if(not(vacaciones or diaDescanso)):
    print("Hoy no se puede salir")

else:
    print("Se puede salir")
