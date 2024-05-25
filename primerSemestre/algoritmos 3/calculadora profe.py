def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    print("Calculadora Básica\n")

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        opcion = int(input("Ingrese su elección (1/2/3/4): "))
        print("Seleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")


        if opcion == 1:
            resultado = suma(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif opcion == 2:
            resultado = resta(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif opcion == 3:
            resultado = multiplicacion(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == 4:
            try:
                resultado = division(num1, num2)
                print("El resultado de la división es:", resultado)
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero. Por favor, ingrese un divisor diferente de cero.\n")
                continue
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).\n")
            continue

    except ValueError:
        print("Error: Por favor, ingrese un valor numérico.\n")
        continue

    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break