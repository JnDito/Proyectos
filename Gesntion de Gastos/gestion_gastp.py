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

while True:
    opcion = input("Ingrese una opción:\n" \
    "1. Registrar Ingreso\n" \
    "2. Registrar Egreso\n" \
    "3. Mostrar Gastos\n" \
    "4. Mostrar Montos Totales\n" \
    "5. Salir\n")

    if opcion == "1":
        print("\n-----Registrar Ingreso-----")
        monto, descripcion = ingresar_monto()
        ingreso.append((descripcion, monto))
        total_ingresos += monto
        saldo += monto

    elif opcion == "2":
        print("\n-----Registrar Egreso-----")
        monto, descripcion = ingresar_monto()
        gastos.append((descripcion, monto))
        total_egresos += monto
        saldo -= monto

    elif opcion == "3":
        print(f"\n-----Gastos-----\n")
        for descripcion, monto in gastos:
            print(f"{descripcion}: S/. {monto}")
    elif opcion == "4":
        print(f"\n-----Montos Totales-----\n")
        print(f"Total Ingresos: S/. {total_ingresos}")
        print(f"Total Egresos: S/. {total_egresos}")
        print(f"Saldo: S/. {saldo}")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.\n")