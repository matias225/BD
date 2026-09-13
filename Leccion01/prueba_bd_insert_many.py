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
            valores = (
                ("Matias", "Romani", "matias@gmail.com"),
                ("Franco", "Romani", "franco@gmail.com"),
                ("Pipis", "Trello", "pipistrello@gmail.com")
            )
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print("Error {}".format(e))
finally:
    conexion.close()
