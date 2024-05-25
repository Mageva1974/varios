print("PUESTO DE VOTACION, LOS REVOLCADOS")
print("******************************************************************")

cedula = []
voto =input("Desea votar en estas elecciones. si = s O no = n : ").lower()
while voto == "s":
    ced=input("Ingrese su numero de cedula: ")
    while len(ced) >= 10:
            print("El numero de cedula debe ser de 10 digitos")
            ced=input("Ingrese su numero de cedula correctamente: ")
    pass
    cedula.append(ced)
    voto = input("desea ingresar otro numero de cedula - si = s O no = n: ")
    pass
print(cedula)

print("Desea conocer si esta inscrito para las elecciones")
cons =input("Favor ingresar la consulta asi: SI = s O NO = n: ")
while cons == "s":
    ced = input("Favor ingresar el numero de cedula: ")
    if ced in cedula:
        print("usted esta inscrito para votar en estas elecciones")
    else:
        print("usted  *NO* esta inscrito para votar en estas elecciones")
    pass
    cons = input("desea ingresar otro numero de cedula - si = s O no = n: ")



