print("Mi primer calculadora en python")

cal = input("Ingrese la operacion a realizar asi: \n"
            "suma = S o s ; resta = R o r ; multiplicacion = M o m ; division = D o d\n"
            "Favor ingresar la operacion:").lower()
num1 = int(input("Favor ingresar el primer numero de la operacion: "))
num2 = int(input("Favor ingresar el segundo numero de la operacion: "))

match cal:

        case "s":
            suma = num1 + num2
            print(f"La suma de los numeros es: {suma}")
        case "r":
            resta = num1 - num2
            print(f"La resta de los numeros es: {resta}")
        case "m":
            multiplicacion = num1 * num2
            print(f"La multiplicacion de los numeros es: {multiplicacion}")
        case "d":
            division = num1 / num2
            print(f"La division de los numeros es: {division}")

        case _:
            print("Operacion no valida")
