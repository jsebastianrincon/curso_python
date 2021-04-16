print("Ingrese los siguientes datos del libro")

nombre = input("Ingrese nombre del libro:")
id = int(input("Ingrese Id del libro:"))
precio = float(input("Ingrese Precio:"))
envioGratuito = input("Indique si es gratuito (True/False):")

if(envioGratuito == "True"):
    envioGratuito = True
elif (envioGratuito == "False"):
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto"

print("Nombre:", nombre)
print("Id:", id)
print("Precio:", precio)
print("¿Envio Gratuito?", envioGratuito)
