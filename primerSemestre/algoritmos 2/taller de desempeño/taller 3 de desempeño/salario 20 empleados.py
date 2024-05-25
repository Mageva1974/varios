def total(sumsal):
    totsal=sum(sumsal)
    promsal=totsal / len(sumsal)
    return promsal
def inc(salarios,incre):
    sal_incrementado=[salario * (1.25) for salario in salarios]
    return sal_incrementado
def main():
 nombres = []
 totsalarios = []
 for i in range(0,2):
    nombre = input("Ingrese el nombre del trabajador: ")
    sal = int(input("Ingrese el salario del trabajador: "))
    sumsal = totsalarios.append(sal)
    nombres.append(nombre)
    print(f"{i+1}- {nombre}, tiene salario de:$ {sal:,.0f}")

 promedio = total(totsalarios)
 print(f"El promedio de los salario de los trabajadores es: {promedio:,.0f} Euros")
 sal_incrementado=inc(totsalarios,2.5)

 print("** Si se aumentara el salario en un 2.5 % **")

 for i, salario in enumerate(sal_incrementado):
        print(f"El empleado {i + 1}- {nombres[i]} aumentara su salario a {salario:,.0f} Euros")


if __name__ == "__main__":
    main()



