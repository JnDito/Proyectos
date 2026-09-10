import re

dni_usuarios = {}

def registrar_usuario(dato):
    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
    if not re.match(patron, dato):
        print("El dato ingresado no es válido. Debe contener solo letras.")
        return False
    return True

def validar_nombre(nombre):
    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
    
    if re.match(patron, nombre):
        return True
    return False

print("-----Registro de Usuarios-----") 
while True: 
    opcion = int(input("Seleccione una opción:\n" \
                    "1. Registrar Usuario\n" \
                    "2. Buscar Usuario\n" \
                    "3. Salir\n"))
    
    if opcion == 1: 
            print("\n-----Registrar Usuario-----")
            while True:
                dni = input("Ingrese el DNI del usuario: ") 
                if not dni.isdigit() or len(dni) != 8:
                    print("DNI inválido. Debe contener 8 dígitos numéricos.\n")
                    continue
                if dni in dni_usuarios:
                    print("El DNI ingresado ya está registrado. Por favor, ingrese un DNI diferente.\n")
                    continue
                else:
                    break

            while True:
                apellido_paterno = input("Ingrese el apellido paterno del usuario: ").upper()
                if not registrar_usuario(apellido_paterno):
                    continue
                else:
                    break

            while True:
                apellido_materno = input("Ingrese el apellido materno del usuario: ").upper()
                if not registrar_usuario(apellido_materno):
                    continue
                else:
                    break

            while True:
                nombre = input("Ingrese el nombre del usuario: ").upper()
                if nombre.strip() and validar_nombre(nombre):
                    break
                else:
                    continue

            while True:
                email = input("Ingrese el email del usuario: ")
                email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(email_pattern, email):
                    print("Email inválido. Debe tener un formato válido (ejemplo: usuario@dominio.com)\n")
                    continue
                else:
                    break

            dni_usuarios[dni] = {'apellido_paterno': apellido_paterno, 'apellido_materno': apellido_materno, 'nombre': nombre, 'email': email}

            print(f"Usuario {dni} registrado exitosamente.\n")
            
    elif opcion == 2: 
            print("\n-----Buscar Usuario-----") 
            solicitar_dni = input("Ingrese el DNI de usuario: ") 
            if solicitar_dni in dni_usuarios: 
                usuario = dni_usuarios[solicitar_dni]
                apellido_paterno = usuario['apellido_paterno']
                apellido_materno = usuario['apellido_materno']
                print(f"Usuario con DNI {solicitar_dni} encontrado.") 
                print(f"Nombre: {usuario['nombre']} {apellido_paterno} {apellido_materno}\n" 
                    f"Email: {usuario['email']}\n")
            
            else: 
                print(f"Usuario con DNI {solicitar_dni} no encontrado.\n")
                
    else: 
        print("\nSaliendo del programa.\n")
        break
    