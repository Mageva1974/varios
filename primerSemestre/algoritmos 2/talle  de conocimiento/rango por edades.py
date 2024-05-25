print("*favor ingresar las edades de las personas, maximo 10*")
cont20=0
cont30=0
cont40=0
cont60=0

for i in range(0,10):
    edad = int(input("Favor ingresar la edad de la persona: "))
    if edad <= 20:
        cont20 += 1
    if edad <=30:
        cont30 += 1
    if edad <=40:
        cont40 += 1
    if edad <=60:
        cont60 += 1
    else:
        print("la edad que ingreso no es valida")

print(f"Las personas menores de 21 años son: {cont20}")
print(f"Las personas menores de 31 años son: {cont30}")
print(f"Las personas menores de 41 años son: {cont40}")
print(f"Las personas menores de 61 años son: {cont60}")