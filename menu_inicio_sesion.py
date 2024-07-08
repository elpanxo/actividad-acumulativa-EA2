usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

def validar_numero_celular(numero):
    if len(numero) == 9 and numero.startswith('9'):
        return True
    else:
        return False

def validar_correo(correo):
    if '@' in correo:
        return True
    else:
        return False
    
while True:
    print("\n--- Menú de Inicio de Sesión ---")
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")

    opcion_menu_principal = input("Seleccione una opción: ")

    try:
        opcion_menu_principal = int(opcion_menu_principal)
    except ValueError:
        print("Error: Ingrese solo números.")
        continue

    if opcion_menu_principal == 1:
        if usuario1 is None and usuario2 is None and usuario3 is None:
            print("No hay usuarios registrados. Registre un usuario antes de iniciar sesión.")
        else:
            usuario = input("Ingrese usuario: ")
            contrasena = input("Ingrese contraseña: ")

            if (usuario == usuario1 and contrasena == contrasena1) or \
               (usuario == usuario2 and contrasena == contrasena2) or \
               (usuario == usuario3 and contrasena == contrasena3):
                print("Inicio de sesión exitoso.")
                while True:
                    print("\n--- Menú Secundario ---")
                    print("1) Realizar llamada")
                    print("2) Enviar correo electrónico")
                    print("3) Cerrar sesión")

                    opcion_menu_secundario = input("Seleccione una opción: ")

                    try:
                        opcion_menu_secundario = int(opcion_menu_secundario)
                    except ValueError:
                        print("Error: Ingrese solo números.")
                        continue

                    if opcion_menu_secundario == 1:
                        numero_celular = input("Ingrese número de celular (9 dígitos, empieza con 9): ")
                        if validar_numero_celular(numero_celular):
                            print(f"Llamando al número {numero_celular}")
                        else:
                            print("Número de celular inválido.")
                    elif opcion_menu_secundario == 2:
                        correo = input("Ingrese correo electrónico: ")
                        while not validar_correo(correo):
                            print("Correo electrónico inválido.")
                            correo = input("Ingrese correo electrónico: ")
                        mensaje = input("Ingrese mensaje a enviar: ")
                        print(f"Enviando correo a {correo} con mensaje: {mensaje}")
                    elif opcion_menu_secundario == 3:
                        print("Cerrando sesión.")
                        break
                    else:
                        print("Opción inválida. Intente de nuevo.")

            else:
                print("Usuario o contraseña incorrectos.")

    elif opcion_menu_principal == 2:
        if usuario1 is None:
            usuario1 = input("Ingrese nuevo usuario: ")
            contrasena1 = input("Ingrese contraseña: ")
            print("Usuario registrado exitosamente.")
        elif usuario2 is None:
            usuario2 = input("Ingrese nuevo usuario: ")
            contrasena2 = input("Ingrese contraseña: ")
            print("Usuario registrado exitosamente.")
        elif usuario3 is None:
            usuario3 = input("Ingrese nuevo usuario: ")
            contrasena3 = input("Ingrese contraseña: ")
            print("Usuario registrado exitosamente.")
        else:
            print("No es posible registrar más usuarios. Limite alcanzado.")

    elif opcion_menu_principal == 3:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
