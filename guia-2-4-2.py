# Ejercicio 1
num_bultos = int(input("Ingrese la cantidad de bultos: "))

total_pagar = 0
bultos_livianos = 0
bultos_normales = 0

for i in range(1, num_bultos + 1):
    peso = float(input(f"Ingrese el peso del bulto {i} en kg: "))

    if peso >= 1 and peso <= 5:
        total_pagar += 1000  
        bultos_livianos += 1
    elif peso > 5 and peso <= 10:
        total_pagar += 2000  
        bultos_normales += 1
    else:
        print(f"El peso {peso} kg no corresponde a ninguna categoría válida.")

print("\nResumen del envío:")
if bultos_livianos > 0:
    print(f"{bultos_livianos} bulto{'s' if bultos_livianos > 1 else ''} liviano{'s' if bultos_livianos > 1 else ''} $1,000 cada uno")
if bultos_normales > 0:
    print(f"{bultos_normales} bulto{'s' if bultos_normales > 1 else ''} normal{'es' if bultos_normales > 1 else ''} $2,000 cada uno")
print(f"Valor total a pagar: ${total_pagar}")


# Ejercicio 2
num_bultos = int(input("Ingrese la cantidad de bultos: "))

total_pagar = 0
bultos_livianos = 0
bultos_normales = 0

nroBulto = 1

while nroBulto <= num_bultos:
    peso = float(input(f"Ingrese el peso del bulto {nroBulto} en kg: "))

    if peso <= 0:
        print("El peso debe ser un valor positivo. Por favor, ingrese nuevamente.")
        continue  

    if peso >= 1 and peso <= 5:
        total_pagar += 1000  
        bultos_livianos += 1
    elif peso > 5 and peso <= 10:
        total_pagar += 2000  
        bultos_normales += 1
    else:
        print(f"El peso {peso} kg no corresponde a ninguna categoría válida.")

    nroBulto += 1

print("\nResumen del envío:")
if bultos_livianos > 0:
    print(f"{bultos_livianos} bulto{'s' if bultos_livianos > 1 else ''} liviano{'s' if bultos_livianos > 1 else ''} $1,000 cada uno")
if bultos_normales > 0:
    print(f"{bultos_normales} bulto{'s' if bultos_normales > 1 else ''} normal{'es' if bultos_normales > 1 else ''} $2,000 cada uno")
print(f"Valor total a pagar: ${total_pagar}")


# Ejercicio 3
valid_input = False

while not valid_input:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = num1 / num2
        print(f"El resultado de la división {num1} / {num2} es: {resultado}")
        valid_input = True  

    except ValueError:
        print("Error: Ingrese solamente números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    except:
        print("Error inesperado. Inténtelo de nuevo.")