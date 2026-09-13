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
            #conexion.autocommit = False   # Este es el valor por default
            sentencia = "INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = ("Pipistrello", "Giovanni", "pipis@trello")
            cursor.execute(sentencia, valores)

            sentencia = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valores = ("Bachicha", "Romani", "bachi@gmail", 4)
            cursor.execute(sentencia, valores)
except Exception as e:
    #conexion.rollback() se hace automatico si esta dentro de with
    print("Ocurrió un error, se hizo rollback: {}".format(e))
finally:
    conexion.close()
print("Termina la transacción, se hizo commit")
