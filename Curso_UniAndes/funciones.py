def saludar(nombre: str = "Uniandes",  mensaje: str = "Hola desde Python:") ->str:
    #saludo = "Hola desde Python " + str(nombre)
    return mensaje + nombre

saludo = saludar(mensaje="Hola: ")
print(saludo)

#args -> n paramatros posicionales
#kwargs -Z> n paramatros llave:valor

def sumar_numeros(*numeros):
    return sum(numeros)

print(sumar_numeros(1,2,3,4))
print(sumar_numeros(1,2))

def info_personas(**datos):
    for llave,valor in datos.items():
        print(f"llave: {llave}, valor:{valor}")

info_personas(nombre="Juan Sebastian", carrera = "Ingenieria de Sistemas")