frase = input("Favor ingresar la frase o palabra para contar las vocales: ")
voc = "aeiouAEIOU"
cont=0
for i in frase:
    if i in voc:
        cont=cont+1
        print(f"la vocal {i} es la: {cont}")
print(f"la frase tiene {cont} vocales")