print("******** SISTEMA DE INFORMACION DE EMPLEADO ******")
print('\n')
empleado = input("Ingrese nombre de empleado: ")
edad_empleado = int(input("Ingrese edad: "))
salario = float(input("Ingrese salario: "))
esJefe = input("Indique si es jefe de departamento (SI/NO):")

if(esJefe == "SI"):
    esJefe = True
elif (esJefe == "NO"):
    esJefe = False
else:
    esJefe = "Valor incorrecto"
    
print("Nombre Empleado:", empleado)
print("Edad:", edad_empleado)
print("Salario:", salario)
print("Es Jefe", esJefe)