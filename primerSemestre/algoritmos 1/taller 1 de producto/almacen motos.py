print("ALMACEN DE MOTOS LA TORTUGA\n")
marca = input("Favor ingresar la marca de moto a comprar: ")
valor =int(input("Favor ingresar el  valor de la moto: "))
if marca=="honda":
    desc=valor * 0.05
    print(f"Las motos {marca}\nTienen un valor de $ {int(valor)}\nDescuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")
elif marca=="yamaha":
    desc=valor * 0.08
    print(f"Las motos {marca}\nTienen un valor de $ {int(valor)}\nDescuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")
elif marca=="suzuki":
    desc=valor * 0.1
    print(f"Las motos {marca}\nTienen un valor de $ {int(valor)}\nDescuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")
else:
    desc=valor * 0.02
    print(f"Las motos {marca}\nTienen un valor de $ {int(valor)}\nDescuento por valor de $ {int(desc)}\nValor final sera:  $ {int(valor-desc)}")


