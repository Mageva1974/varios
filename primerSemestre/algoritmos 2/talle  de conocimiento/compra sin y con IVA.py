print("MOSTRAR VALOR SIN IVA Y CON IVA")
vsin = 0
vcon = 0
for i in range(1,11):
    valor = int(input("ingrese el valor del producto sin iva: "))
    vsin += valor
    vcon += valor + (valor * .19)


print('El valor de los 10 productos  sin IVA es: {:,.2f}'.format(vsin))
print('El valor de los 10 productos  con IVA es: {:,.2f}'.format(vcon))






