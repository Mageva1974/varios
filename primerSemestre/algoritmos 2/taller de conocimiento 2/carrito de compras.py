print("ALMACEN EL CENTAVO")
total = []
def pago(ref,cant):
    match ref:
        case "1":
            pago = cant * 20000
            print(f"El valor a pagar por la  referencia 1 es: {pago}")
            total.append(pago)
        case "2":
            pago = cant * 30000
            print(f"El valor a pagar por la  referencia 2 es: {pago}")
            total.append(pago)
        case "3":
            pago = cant * 10000
            print(f"El valor a pagar por la  referencia 3 es: {pago}")
            total.append(pago)
        case\
            "4":
            pago = cant * 40000
            print(f"El valor a pagar por la  referencia 4 es: {pago}")
            total.append(pago)
        case "5":
            pago = cant * 20000
            print(f"El valor a pagar por la  referencia 5 es: {pago}")
            total.append(pago)
        case "6":
            pago = cant * 20000
            print(f"El valor a pagar por la  referencia 6 es: {pago}")
            total.append(pago)

def main():
    print("**** ARTICULOS ****")
    print("1 - plato pando. valor : $ 20.000")
    print("2 - plato sopt. valor :  $ 30.000")
    print("3 - plato tinto. valor : $ 10.000")
    print("4 - plato plano. valor : $ 40.000")
    print("5 - plato pando. valor : $ 20.000")
    print("6 - plato pando. valor : $ 20.000")

    ref = input("Favor ingresar la referencia a comprar: ")
    cant = int(input("Favor ingresar la cantidad a comprar:"))

    a_pagar = pago(ref,cant)

    comprar =input("Desea adicionar otra referencia al carrito,"
                   " si su respuesta es si escriba S : ").lower()
    while comprar == "s":
        ref = input("Favor ingresar la referencia a comprar: ")
        cant = int(input("Favor ingresar la cantidad a comprar:"))
        a_pagar = pago(ref,cant)
        comprar =input("Desea adicionar otra referencia al carrito,"
                       " si su respuesta es si escriba S : ").lower()
        pass

    suma = sum(total)
    print(f"El total a pagar es de: {suma}")

if __name__ == "__main__":
        main()