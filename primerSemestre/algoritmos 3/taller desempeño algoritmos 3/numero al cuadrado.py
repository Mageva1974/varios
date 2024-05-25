total = []

def Cuadrado(num):
    resultado = num**2
    total.append(resultado)
    return resultado

def main():
    print("CALCULADORA AL CUADRADO")
    num = int(input("Ingrese el numero que desea elevar al cuadrado: "))
    operacion = Cuadrado(num)

    print(f"El cuadrado del numero que ingresastes es: {operacion} ")

    elevado = input("Desea ingresar otro numero,"
                    " si su respuesta es si escriba S : ").lower()
    while elevado == "s":
        num =int(input("Favor ingresar el numero que desea elevar: "))
        operacion = Cuadrado(num)
        print(f"El cuadrado del numero que ingresastes es: {operacion} ")
        elevado = input("Desea ingresar otro numero,"
                        " si su respuesta es si escriba S : ").lower()
        pass
















if __name__ == "__main__":
        main()