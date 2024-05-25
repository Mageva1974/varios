def Fahrenheit(temp):
    temperatura = ((temp)-32) * 5/9
    return temperatura
def Celsius(temp):
    temperatura = ((temp) * 9/5) + 32
    return temperatura


print("CONVERSOR DE TEMPERATURA **LOS GRADOS**")
print("1 - O° Fahrenheit a Celsius")
print("2 - Celsius a Fahrenheit")
temp = float(input("Ingrese la temperatura:"))
op = float(input("Ingrese la opcion: "))
if (op == 1):
    temperatura= Fahrenheit(temp)
    print(f"la temperatura en grados Celsius es: {temperatura:.2f}")
elif (op == 2):
    temperatura= Celsius(temp)
    print(f"la temperatura en grados Fahrenheit es: {temperatura:.2f}")
else:
    print("error fijese en las opciones, CIEGO")
