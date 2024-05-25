"""try:
    x = 10
    y = 20
    z = x + y
    # Error de sintaxis, falta el dos puntos al final de la declaración if
    if z > 15:
        print("El resultado es mayor que 15")
except SyntaxError as e:
    print("Error de sintaxis:", e)



try:
    for i in range(5):
    # Error de indentación, falta indentar la línea print
     print(i)
except IndentationError as e:
    print("Error de indentación:", e)"""

# try:
#
#     print(x)  # x no está definido
# except NameError as e:
#     print("Error de nombre:", e)

#try:
# Código que puede causar un error
# x = 10 / 0
#except ZeroDivisionError:
# Código a ejecutar si se produce un error de división por cero
#        print("Error: División por cero")
#pass
"""
while True:
    try:
        valor1=int(input("Ingrese primer valor:"))
        valor2=int(input("Ingrese segundo valor:"))
        suma=valor1+valor2
        print("La suma es",suma)
    except ValueError:
        print("debe ingresar números.")
    respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break"""

while True:
    try:
        valor1=int(input("Ingrese primer valor:"))
        valor2=int(input("Ingrese segundo valor:"))
        suma=valor1+valor2
        print("La suma es",suma)
    except ValueError:
        print("debe ingresar números.")
    respuesta=input("Desea ingresar otro par de valores?[s/n]")
    if respuesta=="n":
        break
