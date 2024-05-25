def mayor(nom, edad):
 cmayor = 0






def main():
 print("* * CENTRO DE EDADES * *")
 edades = {}
 cant = int(input("Favor ingresar la cantidad de personas: "))
 for i in range(0, cant):
      nom = input("Ingrese el nombre de la persona # {}: ".format(i + 1))
      edad = (input("Favor ingresa la edad de la persona a guardar: "))
      edades[nom] = edad
      mayores = mayor(nom, edad)
 print(edades)





if __name__ == '__main__':
    main()


