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
            sentencia = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valores = ("Matias","Romani", "mati@gmail.com", 3)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros actualizados: {registros_actualizados}")
except Exception as e:
    print("Error {}".format(e))
finally:
    conexion.close()
