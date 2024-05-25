print("EMPRESA LA ENLATADA")
nom=input("Favor ingresar el nombre del trabajador: ")
sal=int(input("Ingrese el salario: "))
dias=int(input("Ingrese los dias trabajados: "))
pagar=(sal/30)*dias
if sal<1300000:
    print(f"{nom}, Debes pedir un aumento")
elif sal==1300000:
    print(f"{nom}, Estas bien")
else:
    print(f"{nom}, Prestame unos pesitos")
