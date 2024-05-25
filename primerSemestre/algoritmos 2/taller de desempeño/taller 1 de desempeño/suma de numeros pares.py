lis = []
print("** SUMA SOLAMENTE DE NUMEROS PARES **")
num = int(input("Favor ingresar la cantidad de numeros que desea ingresar: "))
supar = 0
for i in range(0,num):
    num = int(input("Favor ingresar un numero: "))
    lis.append(num)
    if num % 2 == 0:
        supar += num
print(f"La suma de los numeros pares es: {supar}")

