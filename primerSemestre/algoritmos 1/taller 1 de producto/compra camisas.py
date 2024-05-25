print("Almacen la camiseria")
print("Calcularemos el valor de la compra de varias camisas")
cant=int(input("Favor ingresar la cantidad de camisas a comprar: "))
precio=float(input("Favor ingresar el precio de una camisa: "))

if cant<3:
    pago=(cant*precio)-(cant*precio)*.1
    print(f"el pago de las camisas es: {pago}")
else:
    pago=(cant*precio)-(cant*precio)*.2
    print(f"el pago de las camisas es: {pago}")
