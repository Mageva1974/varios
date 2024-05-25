def Suma(n1, n2):
    return n1 + n2

def Edad(actual,naci):
    edad=int(actual-naci)
    return edad

def par(nu):
    if nu % 2 == 0:
        nu=print(f"{nu} es par")
    else:
        nu=print(f"{nu} es impar")

def cuadrado(m):
    area=m*m
    return area

def Triangulo(b,h):
    area=b*h/2
    return area

while True:
    print("**MENU PRINCIPAL**")
    print("1. Saludar")
    print("2. Suma de 2 numeros")
    print("3. Calcular la edad")
    print("4. Indice de masa corporal")
    print("5. Hallar numero par o impar")
    print("6. Hallar el area de un cuadrado")
    print("7. Hallar el area de un triangulo")
    print("8. Salir")
    op = input("Favor seleccione una de las siguientes opciones:")

    if op=="1":
        print("Hola mundo")
    elif op=="2":
        n1 = int(input("Favor ingresar el numero 1: "))
        n2 = int(input("Favor ingresar el numero 2: "))
        resultado = Suma(n1,n2)
        print(resultado)
    elif op=="3":
        actual=int(input("Favor ingresar el año de fallecimiento: "))
        naci= int(input("Favor ingresar el año en que nacio la persona: "))
        edad=Edad(actual,naci)
        print(edad)
    elif op=="4":
        peso = float(input("favor ingresar su peso: "))
        altura = float(input("favor ingresar su altura: "))
        masa = peso / (altura ** 2)
        print(f"su masa corporal es: {masa:.1f}")
    elif op=="5":
        nu=int(input("Favor ingresar el numero que deseas saber si es par o impar: "))
        pare=par(nu)
    elif op=="6":
        m=int(input("Favor ingresar el lado del cuadrado: "))
        area=cuadrado(m)
        print(f"El area del cuadrado es: {area}")
    elif op=="7":
        base=int(input("Favor ingresar la base del triangulo: "))
        altura=int(input("Favor ingresar la altura del triangulo: "))
        area=Triangulo(base,altura)
        print(f"El area del triangulo es: {area}")
    elif op == '8':
        print(f"Saliendo del programa.")
        break
    else:
        print("No existe la opcion elegida, seleccione alguna opcion del 1 al 8")







