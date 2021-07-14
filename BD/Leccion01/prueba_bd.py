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
            # sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            # sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2,3,4)'
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1, 2, 3),)
            entrada = input(
                'Ingrese los id a buscar (Separados por comas):')
            llaves_primarias = (tuple(entrada.split(',')),)
            # Envio de registro en forma de tupla
            cursor.execute(sentencia, llaves_primarias)
            # Muestra un solo registro
            registros = cursor.fetchall()
            for registros in registros:
                # registros = cursor.fetchone()
                print(registros)
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()
