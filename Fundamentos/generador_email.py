# Sistemas generador de email
print("\n")
print("*** SISTEMA GENERADOR DE EMAILS ***")
print("\n")
nombre = input(f"Ingrese Nombres y Apellidos: ")
empresa = input(f"Ingrese nombre de la empresa: ")
dominio = input(f"Ingrese dominio: ")

concatenacion_correo = nombre[9]


# Quitar espacios en blanco al inicio y al final
nombre_usuario = nombre.strip()
nombre_usuario = nombre_usuario.replace(' ','.')

# Convertir a minusculas
nombre_usuario = nombre_usuario.lower()

#Convertir empresa a minusculas
nombre_empresa = empresa.strip()
nombre_empresa = nombre_empresa.lower()
nombre_empresa = nombre_empresa.replace(' ','')

#Convertir a minusculas dominio

dominio = dominio.strip()
dominio = dominio.lower()
dominio = dominio.replace(' ','')

print("\n")
correo = ''.join([nombre_usuario,'@',nombre_empresa,'',dominio])
print (f'El email generado es: ',correo)
print("\n")