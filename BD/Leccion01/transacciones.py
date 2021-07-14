import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Juana', 'Martinez', 'jmartinez@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Antonio', 'Sosa', 'antoniososa@gmail.com', 21)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo rollback de la transaccion :{e}')
finally:
    conexion.close()
print('Fin de la transaccion, se hizo commit')
