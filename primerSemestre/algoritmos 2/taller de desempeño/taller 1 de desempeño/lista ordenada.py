li = []
cant=int(input("favor ingresar la cantidad de pesonas en la lista: "))
for i in range(0, cant):
    nom=input("Ingrese nombre: ")
    li.append(nom)
li.sort()
print(li)

