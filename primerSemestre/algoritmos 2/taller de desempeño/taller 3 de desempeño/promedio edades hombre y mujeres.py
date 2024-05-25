conth = 0;acumh = 0;contm = 0;acumm = 0
def Prohombre(acumh, conth):
    promh = acumh / conth
    return promh
def Promujer(acumm, contm):
    promm = acumm / contm
    return promm
def main():
    """ ** promedio de edades de mujeres y hombres ** """

cant = int(input("Favor ingresar la cantidad de personas a promediar edades asi:\n"
                 "1 -Hombres, 2-Mujeres:  "))

for i in range(0,cant):
    genero = float(input("Ingrese el genero de la persona a promediar: "))
    edad = float(input("Ingrese la edad: "))


    if genero == 1:
        acumh = acumh+edad
        conth += 1
    else:
        acumm = acumm + edad
        contm += 1

tothombre = Prohombre(acumh, conth)
totmujer = Promujer(acumm, contm)

print(f"El promedio de edades de los hombres es: {tothombre}")
print(f"El promedio de edades de las mujeres es: {totmujer}")


if __name__ == "__main__":
    main()


