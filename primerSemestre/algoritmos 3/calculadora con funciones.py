def Total(cal,num1,num2):

     match cal:
            case "s":
                total = num1 + num2
                print(f"La suma de los numeros es: {total}")
            case "r":
                total = num1 - num2
                print(f"La resta de los numeros es: {total}")
            case "m":
                total = num1 * num2
                print(f"La multiplicacion de los numeros es: {total}")
            case "d":
                total = num1 / num2
                print(f"La division de los numeros es: {total}")

            case _:
                print("Operacion no valida")
     return

while True:
    try:
        cal = str(input("Ingrese la operacion a realizar asi: \n"
                    "suma = S o s ; resta = R o r ; multiplicacion = M o m ; division = D o d\n"
                    "Favor ingresar la operacion:")).lower()
        print("ok")
        pass
    except ValueError:
        print("")
    respuesta = input("Esta usted seguro de la operacion que eligio, desea cambiarla?[s/n]: ")
    if respuesta == "n":
        break

while True:
    try:
        num1 = int(input("Favor ingresar el primer numero de la operacion: "))
        num2 = int(input("Favor ingresar el segundo numero de la operacion: "))
        operacion = Total(cal, num1, num2)
        break
    except ValueError:
     print("Solo se aceptan numeros")
    respuesta = input("Usted desea ingresar los valores nuevamente?[s/n]: ")
    if respuesta == "n":
     break

print("saliendo")

