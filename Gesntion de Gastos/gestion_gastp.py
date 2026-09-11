import json as js
import datetime

total_ingresos = 0
total_egresos = 0
saldo = 0
gastos = []
ingreso = []

def ingresar_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            if monto <= 0:
                print("El monto debe ser mayor a cero. Intente nuevamente.\n")
                continue
            descripcion = input("Ingrese una descripción del monto: ")
            return monto, descripcion
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor valido.\n")

def validar_fechaingresa(fecha_texto):
    try:
        datetime.datetime.strptime(fecha_texto, "%d/%m/%Y")
        return True
    except ValueError:
        return 

def ingresar_fecha():
    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
    while not validar_fechaingresa(fecha):
        print("Fecha inválida. Por favor, ingrese una fecha válida en el formato dd/mm/aaaa.")
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
    return fecha

while True:
    opcion = input("Ingrese una opción:\n" \
    "1. Registrar Ingreso\n" \
    "2. Registrar Egreso\n" \
    "3. Mostrar Ingresos\n" \
    "4. Mostrar Gastos\n" \
    "5. Mostrar Montos Totales\n" \
    "6. Salir\n")

    if opcion == "1":
        print("\n-----Registrar Ingreso-----")
        fecha = ingresar_fecha()
        monto, descripcion = ingresar_monto()
        ingreso.append((fecha, descripcion, monto))
        total_ingresos += monto
        saldo += monto
        print(f"Ingreso registrado: {fecha} - {descripcion}: S/. {monto}\n")

    elif opcion == "2":
        print("\n-----Registrar Egreso-----")
        fecha = ingresar_fecha()
        monto, descripcion = ingresar_monto()
        gastos.append((fecha, descripcion, monto))
        total_egresos += monto
        saldo -= monto
        print(f"Egreso registrado: {fecha} - {descripcion}: S/. {monto}\n")
    elif opcion == "3":
        print(f"\n-----Ingresos-----\n")
        for fecha, descripcion, monto in ingreso:
            print(f"{fecha} - {descripcion}: S/. {monto}\n")

    elif opcion == "4":
        print(f"\n-----Gastos-----\n")
        for fecha, descripcion, monto in gastos:
            print(f"{fecha} - {descripcion}: S/. {monto}\n")
    elif opcion == "5":
        print(f"\n-----Montos Totales-----\n")
        print(f"Total Ingresos: S/. {total_ingresos}")
        print(f"Total Egresos: S/. {total_egresos}")
        print(f"Saldo: S/. {saldo}\n")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.\n")