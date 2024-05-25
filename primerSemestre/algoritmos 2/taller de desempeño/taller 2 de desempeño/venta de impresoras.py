print("***  LA CASA DE LAS IMPRESORAS   ***")
vlimp=80000
iva = 1.19

print("Favor ingresar la cantidad de impresoras que desea comprar: ")
cant = float(input())
while cant <0:
    print("La cantidad debe ser mayor a 0 ")
    cant = float(input())
    pass

print("Ingrese su pago asi: 1 Contado- 2 Tarjeta de credito- 3 Bono de regalo")
fpago = float(input())
while fpago >=4:
    print("ERROR AL INGRESAR SU TIPO DE PAGO")
    print("Ingrese su pago asi: 1 Contado- 2 Tarjeta de credito- 3 Bono de regalo")
    fpago = int(input())
    pass


match fpago:
    case 1:
        vlunit = vlimp * 1.19
        vltot = (vlimp * cant) * 1.19
        desc = vltot * .1
        totpagar = (vlimp - desc)
        print(f"La cantidad de impresoras que compro son: {cant}")
        print(f"El valor unitario de la inpresora es: {vlunit:.0f}")
        print(f"El valor sin descuento es: {vltot:.0f}")
        print("La forma de pago es: Contado")
        print(f"El descuento es: {desc:.0f}")
        print(f"Su total a pagar es de: {totpagar:.0f}")
    case 2:
        vlunit = vlimp * 1.19
        vltot = (vlimp * cant) * 1.19
        desc = vltot * .05
        totpagar = (vlimp - desc)
        print(f"La cantidad de impresoras que compro son: {cant}")
        print(f"El valor unitario de la inpresora es: {vlunit:.0f}")
        print(f"El valor sin descuento es: {vltot:.0f}")
        print("La forma de pago es: Tarjeta de credito")
        print(f"El descuento es: {desc:.0f}")
        print(f"Su total a pagar es de: {totpagar:.0f}")
    case 3:
        vlunit = vlimp * 1.19
        vltot = (vlimp * cant) * 1.19
        desc = vltot * .15
        totpagar = (vlimp - desc)
        print(f"La cantidad de impresoras que compro son: {cant}")
        print(f"El valor unitario de la inpresora es: {vlunit:.0f}")
        print(f"El valor sin descuento es: {vltot:.0f}")
        print("La forma de pago es: Bono de regalo")
        print(f"El descuento es: {desc:.0f}")
        print(f"Su total a pagar es de: {totpagar:.0f}")
















