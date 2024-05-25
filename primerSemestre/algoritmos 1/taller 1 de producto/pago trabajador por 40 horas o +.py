print("Empresa la mejora\n")
trab=input("Favor ingresar el nombre del trabajador: ")
horas=int(input("Favor ingresar las horas trabajadas: "))
hora=int(input("favor ingresar el valor de la hora: "))
if horas<=40:
    pago=(horas*hora)
    print(f"El pago de {trab} es: {pago}")
else:
    pago=(hora*40)+(((horas-40)*hora)*1.5)


    print(f"El pago de {trab} es: {pago}")
