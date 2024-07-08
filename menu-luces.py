luces_patio_encendidas = False
luces_sala_encendidas = False
luces_pasillo_encendidas = False
luces_jardin_encendidas = False

def alternar_luces(estado_actual):
    return not estado_actual 

while True:
    print("\n--- Menú de control de luces ---")
    print("1.- Encender/Apagar luces Patio")
    print("2.- Encender/Apagar luces Sala")
    print("3.- Encender/Apagar luces Pasillo")
    print("4.- Encender/Apagar luces Jardín")
    print("5.- Encender todo")
    print("6.- Apagar todo")
    print("7.- Salir del sistema")

    opcion = input("Ingrese la opcion deseada: ")

    try:
        opcion = int(opcion)
        
        if opcion == 1:
            luces_patio_encendidas = alternar_luces(luces_patio_encendidas)
            print("El patio está", "encendido" if luces_patio_encendidas else "apagado")
        elif opcion == 2:
            luces_sala_encendidas = alternar_luces(luces_sala_encendidas)
            print("La sala está", "encendida" if luces_sala_encendidas else "apagada")
        elif opcion == 3:
            luces_pasillo_encendidas = alternar_luces(luces_pasillo_encendidas)
            print("El pasillo está", "encendido" if luces_pasillo_encendidas else "apagado")
        elif opcion == 4:
            luces_jardin_encendidas = alternar_luces(luces_jardin_encendidas)
            print("El jardin está", "encendido" if luces_jardin_encendidas else "apagado")
        elif opcion == 5:
            luces_patio_encendidas = alternar_luces(luces_patio_encendidas)
            luces_sala_encendidas = alternar_luces(luces_sala_encendidas)
            luces_pasillo_encendidas = alternar_luces(luces_pasillo_encendidas)
            luces_jardin_encendidas = alternar_luces(luces_jardin_encendidas)
            print("Todas las luces han sido encendidas.")
        elif opcion == 6:
            luces_patio_encendidas = False
            luces_sala_encendidas = False
            luces_pasillo_encendidas = False
            luces_jardin_encendidas = False
            print("Todas las luces han sido apagadas.")
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero del 1 al 7.")