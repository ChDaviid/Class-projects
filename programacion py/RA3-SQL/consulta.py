import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="liga_futbol"
)


def consultar(sql, datos=()):
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    resultados = cursor.fetchall()
    cursor.close()

    print(f"Resultados de la consulta: {len(resultados)}")
    if len(resultados) == 0:
        print("No hay resultados.")
    for fila in resultados:
        print("  " + " | ".join(str(dato) for dato in fila))



def mostrar_menu():
    print("\n===== LIGA DE FÚTBOL =====")
    print(" 1. Listar todos los equipos")
    print(" 2. Consultar jugadores de un equipo")
    print(" 3. Consultar jugadores por posición")
    print(" 4. Consultar goles de un jugador")
    print(" 5. Consultar jugadores por edad y posición")
    print(" 0. Salir")


opcion = ""


while opcion != "0":
    mostrar_menu()
    opcion = input("\nSelecciona una opción: ")


    if opcion == "1":
        consultar("SELECT nombre FROM Equipo ORDER BY nombre")


    elif opcion == "2":
        equipo = input("Nombre del equipo: ")
        consultar("""SELECT j.nombre, j.posicion, j.edad
                     FROM Jugador j
                     INNER JOIN Equipo e ON j.id_equipo = e.id_equipo
                     WHERE e.nombre = %s""", (equipo,))


    elif opcion == "3":
        posicion = input("Posición: ")
        consultar("SELECT nombre, posicion, edad FROM Jugador WHERE posicion = %s", (posicion,))


    elif opcion == "4":
        jugador = input("Nombre del jugador: ")
        consultar("""SELECT j.nombre, g.minuto
                     FROM Gol g
                     INNER JOIN Jugador j ON g.id_jugador = j.id_jugador
                     WHERE j.nombre = %s
                     ORDER BY g.minuto""", (jugador,))


    elif opcion == "5":
        edad = input("Edad: ")
        posicion = input("Posición: ")
        consultar("SELECT nombre, posicion, edad FROM Jugador WHERE edad = %s AND posicion = %s", (edad, posicion))


    elif opcion == "0":
        print("Hasta luego.")


    else:
        print("Opción no válida.")


conexion.close()