# Eliminar un registro

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
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Ingrese persona a eliminar: ')
            valores = (entrada,)
            # Registro multiple en BD
            cursor.execute(sentencia, valores)
            # conexion.commit
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados:{registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()
