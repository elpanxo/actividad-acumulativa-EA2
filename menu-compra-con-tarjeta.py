print("")
opcion = 0
pago = 100000

while True:
    print("*************** Menu *******************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    print("")

    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except ValueError:
        opcion = 0

    if opcion == 1:
        print("\n---- Pago con tarjeta de crédito ----")
        numero_tarjeta_credito = input("Ingrese el número de tarjeta de crédito: ")
        nombre_titular = input("Ingrese nombre del titular: ")
        mes_vencimiento = input("Ingrese el mes de vencimiento (MM): ")
        año_vencimiento = input("Ingrese el año de vencimiento (YYYY): ")
        print("Procesando pago por tarjeta de crédito...")
    elif opcion == 2:
        print("\n---- Pago con Paypal ----")
        usuario_paypal = input("Ingrese nombre de usuario Paypal: ")
        contraseña_paypal = input("Ingrese su contraseña: ")
        print("Procesando pago por Paypal...")
    elif opcion == 3:
        print("\n ---- Pago por transferencia eléctronica ----")
        print("Datos de transferencia:")
        print("Banco: Banco de Chile")
        print("Numero de cuenta: XXXX-XXXX-XXXX-XXXX")
        codigo_referencia = input("Ingrese código de referencia: ")
        print("Procesando pago por transferencia eléctronica...")
    elif opcion == 4:
        print("Pago cancelado")
        
    elif opcion == 5:
        print("Hasta pronto...")
        break

    else:
        print("Opción no válida")

print("")
print("Muchas gracias por su compra")
print("")