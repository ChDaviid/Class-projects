#lanzar dado
from logging import exception


def Lanzar_dado():
    import random
    return random.randint(1, 6)

#Elegir azar
def elegir_azar(lista):
 import random
 return random.choice(lista)

#Raíz cuadrada
def raiz_cuadrada(numero):
    import math
    return math.sqrt(numero)

#cajas necesarias
def cajas_necesarias(cantidad, capacidad_caja):
    import math
    return math.ceil(cantidad / capacidad_caja)


#mostrar fecha y hora actual
from datetime import datetime
def mostrar_fecha_hora_actual():
    fecha_hora_actual = datetime.now()
    return fecha_hora_actual.strftime("%d-%m-%Y %H:%M:%S")

#Cuenta atrás
def cuenta_atras(numero):
    import time
    for i in range(numero,0,-1):
        print(i)
        time.sleep(1) 
    print("¡Tiempo terminado!")

#Mezclar lista
def mezclar_lista(lista):
    import random
    random.sample(lista, len(lista))
    return lista

#elegir 3 ganadores
def elegir_ganadores(lista):
    lista = input("Ingrese en la lista 5 nombres separados por comas: ").split(",")
    import random
    return random.sample(lista, 3)

#generar número decimal
def generar_numero_decimal():
    numero_decimal1 = float(input("Ingrese un número decimal: "))
    numero_decimal2 = float(input("Ingrese otro número decimal: "))
    if numero_decimal1 > numero_decimal2:
        print("El primer número tiene que ser menor que el segundo número.")
        return None
    import random
    return random.uniform(numero_decimal1, numero_decimal2)

#calcular factorial
def calcular_factorial(numero):
    numero = int(input("Ingrese un número entero no negativo: "))
    if numero < 0:
        print("El número debe ser no negativo.")
        return None
    import math
    return math.factorial(numero)


#calcular bolas completas
def calcular_bolas(cantidad, capacidad_bolsa):
    cantidad = int(input("Ingrese la cantidad de bolas no negativa: "))
    capacidad_bolsa = int(input("Ingrese la capacidad de la bolsa no negativa: "))
    if cantidad < 0 or capacidad_bolsa <= 0:
        print("La cantidad debe ser no negativa y la capacidad de la bolsa debe ser positiva.")
        return None
    import math
    return math.floor(cantidad / capacidad_bolsa)

#Analizar notas
def analizar_notas(notas):
    notas = input("Ingrese 5 notas entre el 0 y el 10 separadas por comas: ").split(",")
    notas = [float(nota) for nota in notas]
    import statistics
    nota_media = statistics.mean(notas)
    mediana = statistics.median(notas)
    print("Nota media:", nota_media)
    print("Nota mediana:", mediana)

#Buscar valores mas frecuentes
import statistics

def buscar_valores_frecuentes(numeros):
    numeros = input("Ingrese una lista de números separados por comas: ").split(",")
    numeros = [int(numero) for numero in numeros]
    try:
        moda = statistics.mode(numeros)
        print("El valor más frecuente es:", moda)
    except statistics.StatisticsError:
        print("No hay un valor más frecuente (todos los valores son igualmente frecuentes).")


#Formatos de fecha
def formato_fecha(fecha):
    ahora = datetime.now()
    texto = ahora.strftime("%d/%m/%Y")
    print("Fecha actual:", texto)


#Calcular fecha futura
from datetime import datetime, timedelta

def fecha_futura(dias):
    dias = int(input("Introduce un número de días: "))
    fecha_actual = datetime.now()
    fecha_futura = fecha_actual + timedelta(days=dias)
    print(f"La fecha futura después de {dias} días será: {fecha_futura.strftime('%d/%m/%Y')}")

#Comprobar año bisiesto
def year_bisiesto(year):
    year = int(input("Introduce un año: "))
    import calendar
    if calendar.isleap(year):
        print(f"El año {year} es bisiesto.")
    else:
        print(f"El año {year} no es bisiesto.")


#Mostrar calendario
import calendar
def mostrar_calendario(year, month):
    year = int(input("Introduce un año: "))
    month = int(input("Introduce un mes (1-12): "))
    if 1 <= month <= 12:
        print(calendar.month(year, month))
    else:
        print("Mes inválido. Debe estar entre 1 y 12.")



while True:

    print("1. Lanzar un dado.")
    print("2. Elegir un Alumno.")
    print("3. calcular la raíz cuadrada de un número.")
    print("4. calcular el número de cajas necesarias para guardar una cantidad de elementos.")
    print("5. Mostrar la fecha y hora actual.")
    print("6. Realizar una cuenta atrás.")
    print("7. Mezclar una lista.")
    print("8. Elegir 3 ganadores de una lista.")
    print("9. Generar un número decimal aleatorio entre dos números.")
    print("10. Calcular el factorial de un número.")
    print("11. Calcular cuántas bolas completas caben en una bolsa.")
    print("12. Analizar notas.")
    print("13. Buscar los valores más frecuentes en una lista de números.")
    print("14. Mostrar la fecha en formato dd/mm/yyyy.")
    print("15. Calcular la fecha futura a partir de un número de días.")
    print("16. Comprobar si un año es bisiesto.")
    print("17. Mostrar el calendario de un mes y año específico.")
    print("18. Salir")

    try:
        print("--------------------------------")
        opcion = int(input("Ingrese la opción que desea realizar: "))
        print("--------------------------------")
        if opcion not in range(1, 19):
            raise ValueError
    except ValueError:
        print("--------------------------------")
        print("Error: Por favor, ingrese una opción válida del 1 al 18.")
        print("--------------------------------")
        continue

    if opcion == 1:
        print("--------------------------------")
        print("Resultado del lanzamiento del dado:", Lanzar_dado())
        print("--------------------------------")
    elif opcion == 2:
        print("--------------------------------")
        try:
            lista_alumnos = input("Ingrese los nombres de los alumnos separados por comas: ").split(",")
        except ValueError:
            print("Error: Por favor, ingrese los nombres separados por comas.")
        print("Alumno elegido al azar:", elegir_azar(lista_alumnos))
        print("--------------------------------")
    elif opcion == 3:
        print("--------------------------------")
        numero = float(input("Ingrese un número: "))
        print("La raíz cuadrada de", numero, "es:", raiz_cuadrada(numero))
        print("--------------------------------")
    elif opcion == 4:
        print("--------------------------------")
        cantidad = int(input("Ingrese la cantidad de elementos: "))
        capacidad_caja = int(input("Ingrese la cantidad de elementos por caja: "))
        print("Número de cajas necesarias:", cajas_necesarias(cantidad, capacidad_caja))
        print("--------------------------------")
    elif opcion == 5:
        print("--------------------------------")
        print("Fecha y hora actual:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("--------------------------------")
    elif opcion == 6:
        print("--------------------------------")
        segundos = int(input("Ingrese la cantidad de segundos para la cuenta atrás: "))
        cuenta_atras(segundos)
        print("--------------------------------")
    elif opcion == 7:
        print("--------------------------------")
        lista = input("Ingrese los elementos de la lista separados por comas: ").split(",")
        print("Lista mezclada:", mezclar_lista(lista))
        print("--------------------------------")
    elif opcion == 8:
        print("--------------------------------")
        lista = input("Ingrese los nombres de los participantes separados por comas: ").split(",")
        print("Ganadores:", elegir_ganadores(lista))
        print("--------------------------------")
    elif opcion == 9:
        print("--------------------------------")
        generar_numero_decimal1 = float(input("Ingrese el valor mínimo: "))
        generar_numero_decimal2 = float(input("Ingrese el valor máximo: "))
        print("Número decimal aleatorio:", generar_numero_decimal(generar_numero_decimal1, generar_numero_decimal2))
        print("--------------------------------")
    elif opcion == 10:
        print("--------------------------------")
        numero = int(input("Ingrese un número: "))
        print("El factorial de", numero, "es:", calcular_factorial(numero))
        print("--------------------------------")
    elif opcion == 11:
        print("--------------------------------")
        bolas = int(input("Ingrese la cantidad de bolas: "))
        capacidad_bolsa = int(input("Ingrese la capacidad de la bolsa: "))
        print("Número de bolas completas que caben en la bolsa:", calcular_bolas(bolas, capacidad_bolsa))
        print("--------------------------------")
    elif opcion == 12:
        print("-------------------------------------")
        try:
            notas = input("Ingrese las notas separadas por comas: ").split(",")
            notas = [float(nota) for nota in notas]
            resultado = analizar_notas(notas)
            for clave, valor in resultado.items():
                print(f"{clave}: {valor}")
        except ValueError:
            print("Error: Por favor, ingrese las notas separadas por comas.")
        print("-------------------------------------")
    elif opcion == 13:
        print("-------------------------------------")
        numeros = input("Ingrese los números separados por comas: ").split(",")
        numeros = [int(numero) for numero in numeros]
        buscar_valores_frecuentes(numeros)
        print("-------------------------------------")
    elif opcion == 14:
        print("-------------------------------------")
        formato_fecha(datetime.now())
        print("-------------------------------------")
    elif opcion == 15:
        print("-------------------------------------")
        dias = int(input("Ingrese un número de días: "))
        fecha_futura(dias)
        print("-------------------------------------")
    elif opcion == 16:
        print("-------------------------------------")
        year = int(input("Ingrese un año: "))
        year_bisiesto(year)
        print("-------------------------------------")
    elif opcion == 17:
        print("-------------------------------------")
        year = int(input("Ingrese un año: "))
        month = int(input("Ingrese un mes (1-12): "))
        mostrar_calendario(year, month)
        print("-------------------------------------")
    elif opcion == 18:
        print("Saliendo del programa...")
        break

