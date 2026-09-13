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
            sentencia = "SELECT * FROM personas ORDER BY id_persona"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print("Error {}".format(e))
finally:
    conexion.close()
