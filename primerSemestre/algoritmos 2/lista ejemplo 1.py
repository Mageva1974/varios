lista = []
print("Escribe una palabra: ")
sPalabra = input()
while sPalabra != "":
    lista +=[sPalabra]
    print("Escribe una palabra: ")
    sPalabra = input()
print("Las palabras que a escrito son : %s" % lista)
