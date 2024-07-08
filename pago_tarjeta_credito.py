deuda_tarjeta = 100000

def pago_tarjeta(monto):
    global deuda_tarjeta
    if monto < 0:
        print("Error: El monto ingresado debe ser mayor o igual a cero.")
        return
    
    if monto > deuda_tarjeta:
        print("Error: El monto a pagar excede la deuda actual de la tarjeta.")
        return
    
    deuda_tarjeta -= monto
    print(f"Se realizó un pago de ${monto}. Deuda restante: ${deuda_tarjeta}")

def simulacion_compras():
    total_compras = 0
    while True:
        try:
            monto_compra = float(input("Ingrese el monto de la compra (0 para salir): "))
            if monto_compra < 0:
                print("Error: El monto de la compra debe ser mayor o igual a cero.")
                continue
            elif monto_compra == 0:
                break
            
            total_compras += monto_compra
            print(f"Compra realizada por ${monto_compra}. Total acumulado: ${total_compras}")
        
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    return total_compras

while True:
    print("\n--- Menú Principal ---")
    print("1. Pago de Tarjeta de Crédito")
    print("2. Simulación de Compras")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        try:
            monto_pago = float(input("Ingrese el monto a pagar: "))
            pago_tarjeta(monto_pago)
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    elif opcion == '2':
        total_compras = simulacion_compras()
        deuda_tarjeta += total_compras 
        
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    
    else:
        print("Error: Opción no válida. Seleccione 1, 2 o 3.")