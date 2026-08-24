def calcular_iva(costo: float) ->float:
    return costo * 0.19

compra = int(input("Ingrese costo: "))
iva = calcular_iva(compra)
print("El costo total es: ",compra + iva)