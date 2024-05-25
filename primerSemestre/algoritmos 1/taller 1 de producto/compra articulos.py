print("ALMACEN EL CENTAVO")
print("si los articulos son menores a 3 el pago ser en efectivo")
print("si los articulos son mayores a 2 el pago ser con tarjeta\n")

cant=(int(input("Favor ingresar cuantos articulos va a llevar: ")))
if cant<3:
    print("El pago es en efectivo")
    print("Gracias por su pago")
else:
    print("El pago es con tarjeta")
    print("Gracias por su pago")

