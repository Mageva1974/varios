lista = []
cant = int(input("Ingrese la cantidad de personas de la lista: "))
for i in range(0, cant):
    nom = input("Ingrese un nombre: ")
    lista.append(nom)
lista.sort()
print (lista)

for palabra in lista:
    letra=str(input("Ingrese la primer letra de la palabra que desea conocer: "))
    if palabra [0]==letra:
        print(f"La palabra es: {palabra}")
    break


