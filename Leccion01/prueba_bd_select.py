import psycopg2 as pg

conexion = pg.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="test_db"
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM personas WHERE id_persona IN %s"
            # llaves_primarias = ((1, 2, 3),) tiene que ser una tupla de tuplas
            entrada = input("Ingresa los id's a buscar (separados por comas): ")
            llaves_primarias = (tuple(entrada.split(",")),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print("Error {}".format(e))
finally:
    conexion.close()
