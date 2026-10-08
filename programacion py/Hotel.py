habitaciones = [
    {
        "numero": 101,
        "planta": 1,
        "tipo": "Individual",
        "precio": 50,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 102,
        "planta": 1,
        "tipo": "Doble",
        "precio": 80,
        "ocupadaPor": {
            "nombre": "Ana García",
            "dni": "12345678A",
            "fechaEntrada": "2026-10-07",
            "noches": 3
        }
    },
    {
        "numero": 103,
        "planta": 1,
        "tipo": "Doble",
        "precio": 80,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 104,
        "planta": 1,
        "tipo": "Suite",
        "precio": 150,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 105,
        "planta": 1,
        "tipo": "Individual",
        "precio": 50,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 201,
        "planta": 2,
        "tipo": "Doble",
        "precio": 85,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 202,
        "planta": 2,
        "tipo": "Suite",
        "precio": 160,
        "ocupadaPor": {
            "nombre": "Carlos López",
            "dni": "87654321B",
            "fechaEntrada": "2026-10-06",
            "noches": 5
        }
    },
    {
        "numero": 203,
        "planta": 2,
        "tipo": "Individual",
        "precio": 55,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 204,
        "planta": 2,
        "tipo": "Doble",
        "precio": 85,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 205,
        "planta": 2,
        "tipo": "Suite",
        "precio": 160,
        "ocupadaPor": "Libre"
    }
]


while True:
    print("1. Registrar entrada: ")
    print("2. Registrar salida: ")
    print("3. Listar habitaciones ocupadas: ")
    print("4. Listar habitaciones libres: ")
    print("5. Resumen del Hotel: ")
    print("6. Salir: ")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cliente {
            "nombre": input("Introduce el nombre del cliente: "),
            "dni": input("Introduce el DNI del cliente: "),
            "fechaEntrada": input("Introduce la fecha de entrada: "),
            "noches": int(input("Introduce el número de noches: "))
        }