usuarios = {}
dni_usuarios = {}
email_usuarios = {}

print("-----Registro de Usuarios-----") 
while True: 
    opcion = int(input("Seleccione una opción:\n" \ 
                    "1. Registrar Usuario\n" \ 
                    "2. Buscar Usuario\n" \ 
                    "3. Salir\n")) 
    if opcion == 1: 
        print("\n-----Registrar Usuario-----")
        dni = input("Ingrese el DNI del usuario: ") 
        if dni in dni_usuarios: 
            print(f"Error: El DNI {dni} ya está registrado.") 
            continue 
        else: dni_usuarios[dni] = None 
        nombre = input("Ingrese el nombre del usuario: ") 
        email = input("Ingrese el email del usuario: ") 
        usuarios[nombre] = dni 
        email_usuarios[email] = dni 
        print(f"Usuario {dni} registrado exitosamente.\n") 
    elif opcion == 2: 
        print("\n-----Buscar Usuario-----") 
        solicitar_dni = input("Ingrese el DNI de usuario: ") 
        if solicitar_dni in dni_usuarios: 
            print(f"Usuario con DNI {solicitar_dni} encontrado.") 
            print(f"Nombre: {next((nombre for nombre in usuarios if usuarios[nombre] == solicitar_dni))}\n " 
                f"Email: {next((email for email in email_usuarios if email_usuarios[email] == solicitar_dni))}\n") 
        else: 
            print(f"Usuario con DNI {solicitar_dni} no encontrado.\n") 
    else: 
        print("\nSaliendo del programa.") 
        break