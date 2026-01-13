from random import randint

print('*** SISTEMA GENERADOR DE ID UNICO ***')

nombre = input('¿Cual es tu nombre?: ')
apellido = input('¿Cual es tu apellido?: ')
anio_nacimiento = ((input('¿Cual es tu año de nacimiento?: ')))

mayuscula_nombre = nombre.strip().upper()
mayuscula_apellido = apellido.strip().upper()

dos_primeras_nombre = mayuscula_nombre[0:2]
dos_primeras_apellido = mayuscula_apellido[0:2]
dos_ultimas_anio = anio_nacimiento.strip()[2:4]

numero_aleatorio = str(randint(1000,9999))
cadena_final = dos_primeras_nombre,dos_primeras_apellido,dos_ultimas_anio,numero_aleatorio

cadena_final_sin_espacios = (''.join(cadena_final))
print(f'Hola Tu nuevo numero de identificación generado por el sistema es:{cadena_final_sin_espacios}')
