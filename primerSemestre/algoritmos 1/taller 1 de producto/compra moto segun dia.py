print("vamos a cotizar una moto, segun el dia, tambien dia feriado y hay descuentos")
dia=(input("ingrese el dia que se va a comprar la moto: "))
valor=int(input("Ingresar el valor de la moto: "))
if dia=="martes":
    desc=valor * 0.12
    print(f"La moto Tienen  Descuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")
elif dia=="sabado":
    desc=valor * 0.18
    print(f"La moto Tienen  Descuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")
elif dia=="feriado":
    desc=valor * 0.25
    print(f"La moto Tienen  Descuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")
else:
      print(f"La motos no tiene Descuento\nValor final sera:  $ {int(valor)}")