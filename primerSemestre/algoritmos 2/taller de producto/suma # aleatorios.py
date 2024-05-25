import random
def suma(num1, num2):
    suma = num1 + num2
    return suma

def main():

 print("Realizar la suma de 2 numeros que la computadora nos da: ")
 num1 = random.randint(1,100)
 num2 = random.randint(1,100)

 sumanum =suma(num1,num2)

 total =int(input(f"La suma de los numeros {num1} + {num2} es: "))

 while total >= 0:
     if total == sumanum:
        print(f"La suma de los numeros es: * CORRECTO *")
        break
     else:
        print(f"La suma de los numeros es: * INCORRECTO *")
        print("Favor ingresar nuevamente la contraseña")
        print("----------------------------------------------")
        total = int(input(f"La suma de los numeros {num1} + {num2} es: "))

if __name__ == "__main__":
         main()