import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="liga_futbol"
)

print("Conexión establecida correctamente")
conexion.close()

