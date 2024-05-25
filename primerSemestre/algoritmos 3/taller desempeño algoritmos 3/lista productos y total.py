
receta = {}

def main():
    print("Bienvenido a * Usted mismo lo hace*")
    cant = int(input("Favor ingresar la cantidad de productos que va a usar en su receta: "))
    for i in range(0, cant):
            produto = input("Ingrese el alimento # {}:  ".format(i+1))
            val = int(input("Ingrese el valor del alimento # {}: ".format(i+1)))
            receta[produto] = val
    print("La receta lleva los siguientes ingredientee con sus respectivos valores")
    print(receta)
    total = sum(receta.values())
    print("El costo total de la receta es: ",total)
















if __name__ == "__main__":
        main()