print("Favor ingresar 3 numeros y decir cual es mayor: ")
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
n3=int(input("Ingrese el tercer numero: "))

if (n1!=n2)and(n2!=n3)and(n1!=n3):
    def Mayor(n1,n2,n3):
        mayor=0
        if n1>n2 and n1>n3:
            mayor=n1
        elif n2>n1 and n2>n3:
            mayor=n2
        elif n3>n1 and n3>n2:
            mayor=n3
        return mayor
    resultado_mayor=Mayor(n1,n2,n3)
    print(f"El numero mayor es: {resultado_mayor}")

else:
    print(f"Algunos numeros son iguales ")










