print("Empresa la unica")
nom=(input("Favor ingresar el nombre: "))
pago=int(input("Favor ingresar el salario del trabajador:"))

if pago<=1000:
    salario=pago-(pago*.1)
    print(f"El salario del trabajador {nom} con descuento es: {salario}")
elif (pago>1000)and(pago<=2000):
    salario=pago-(pago*.05)
    print(f"El salario del trabajador {nom} con descuento es: {salario}")
elif pago>2000:
    salario=pago-(pago*.03)
    print(f"El salario del trabajador {nom} con descuento es: {salario}")
