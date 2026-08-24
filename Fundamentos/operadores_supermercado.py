# Supermercado descuentos
# Condiciones 
# Solicitar # de articulos y si tiene membresia si 
# Si es miembro y tiene mas de 10 articulos entonces tiene descue VIP

print('*** SISTEMA DE DESCUENTOS ***')

num_productos_descuento = int(input("Ingrese numero de articulos: "))
tiene_memebresia = input("¿Tiene membresia? (SI/NO): ")
cantidad_limite = 10

if(tiene_memebresia == "SI"):
   tiene_memebresia = True
elif (tiene_memebresia == "NO"):
    tiene_memebresia = False
else:
    tiene_memebresia = "Valor incorrecto"
condiciones_membresia = num_productos_descuento >= cantidad_limite and tiene_memebresia  
if(condiciones_membresia):
    print("Tiene descuento VIP")
else:
    print("No cuenta con beneficios premium")    
    
