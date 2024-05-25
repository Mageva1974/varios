
def cambio(ref,cant):
    match ref:
        case "1":
            print("1 - dolar a peso colombiano")
            print("2 - peso colombiano a dolar")
            op =input("Favor colocar la operacion a realizar, 1 O 2: ")
            if op == "1":
                pago = cant * 3800
                print(f"El valor a pagar por la transferencia es: {pago}")
            else:
                pago = cant / 3800
                print(f"El valor a pagar por la transferencia es: {pago}")









def main():
    print("**** CAMBIADERO EL DOLAR FALSO ****")
    print("1 - DOLARES")
    print("2 - EUROS")
    print("3 - LIBRA ESTERLINA")


    ref = input("Favor ingresar el numero de la moneda que desea cambiar segun el menu: ")
    cant = int(input("Favor ingresar la cantidad a cambiar:"))

    a_pagar = cambio(ref,cant)

    comprar =input("Desea cambiar otra moneda"
                   " si su respuesta es si escriba S : ").lower()
    while comprar == "s":
        ref = input("Favor ingresar la moneda a cambiar: ")
        cant = int(input("Favor ingresar la cantidad a cambiar:"))
        a_pagar = cambio(ref,cant)
        comprar =input("Desea adicionar otra referencia al carrito,"
                       " si su respuesta es si escriba S : ").lower()
        pass


if __name__ == "__main__":
        main()