# Actualizacion multiple

import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Luisa', 'Martinez', 'luisamartinez@gmail.com', 22),
                       ('Andres', 'Vallejo', 'andresantova669@gmail.com', 21)
                       )
            # Registro multiple en BD
            cursor.executemany(sentencia, valores)
            # conexion.commit
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados:{registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()
