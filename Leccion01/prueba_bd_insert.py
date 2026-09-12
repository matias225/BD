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
            sentencia = "INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = ("Santiago", "Romani", "santiago@gmail.com")
            cursor.execute(sentencia, valores)
            # conexion.commit() se hace solo por estar dentro de un with
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print("Error {}".format(e))
finally:
    conexion.close()
