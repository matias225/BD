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
            sentencia = "DELETE FROM personas WHERE id_persona = %s"
            entrada = input("Ingrese el id de la persona que desea eliminar: ")
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")
except Exception as e:
    print("Error {}".format(e))
finally:
    conexion.close()
