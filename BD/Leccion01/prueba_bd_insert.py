#Insertar registros 

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
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
            valores = ('Maria', 'Martinez', 'mariamartinez@gmail.com')
            cursor.execute(sentencia, valores)
            # conexion.commit
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados:{registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()
