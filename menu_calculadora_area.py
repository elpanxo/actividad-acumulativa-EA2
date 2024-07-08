import math

print("")
print("Calculadora geométrica")
print("")
while True:
    print("*********** Menu ************")
    print("1. Calcular Perímetro")
    print("2. Calcular Área")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    print("")
    
    if opcion == 1:
        print("Calcular Perímetro")
        print("1. Para Círculo")
        print("2. Para Rectángulo")
        print("3. Para Cuadrado")
        print("4. Volver al menú principal")
        opcion2 = int(input("Elija una opción: "))
        print("")
        
        if opcion2 == 1:
            radio = float(input("Ingrese radio del círculo: "))
            perimetro = 2 * math.pi * radio
            print(f"Perímetro del Círculo: {perimetro}")
            print("")
        elif opcion2 == 2:
            altura = float(input("Ingrese altura del rectángulo: "))
            ancho = float(input("Ingrese ancho del rectángulo: "))
            perimetro = 2 * (altura + ancho)
            print(f"Perímetro del Rectángulo: {perimetro}")
            print("")
        elif opcion2 == 3:
            lado = float(input("Ingrese lado del cuadrado: "))
            perimetro = 4 * lado
            print(f"Perímetro del Cuadrado: {perimetro}")
            print("")
        elif opcion2 == 4:
            print("Volviendo al menú principal...")
            print("")
        else:
            print("Elección inválida.")
            print("")
            
    elif opcion == 2:
        print("Calcular Área")
        print("1. Para Círculo")
        print("2. Para Rectángulo")
        print("3. Para Cuadrado")
        print("4. Volver al menú principal")
        opcion3 = int(input("Elija una opción: "))
        print("")
        
        if opcion3 == 1:
            radio = float(input("Ingrese radio del círculo: "))
            area = math.pi * radio ** 2
            print(f"Área del Círculo: {area}")
            print("")
        elif opcion3 == 2:
            altura = float(input("Ingrese altura del rectángulo: "))
            ancho = float(input("Ingrese ancho del rectángulo: "))
            area = altura * ancho
            print(f"Área del Rectángulo: {area}")
            print("")
        elif opcion3 == 3:
            lado = float(input("Ingrese lado del cuadrado: "))
            area = lado ** 2
            print(f"Área del Cuadrado: {area}")
            print("")
        elif opcion3 == 4:
            print("Volviendo al menú principal...")
            print("")
        else:
            print("Elección inválida.")
            print("")
            
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    
    else:
        print("Elección inválida.")
        print("")

print("")
print("¡Gracias por usar la calculadora geométrica!")
print("")
