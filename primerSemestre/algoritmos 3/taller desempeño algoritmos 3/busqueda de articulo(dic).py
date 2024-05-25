
def main():
 print(" * * MERCADO EL CENTAVO FALSO * * ")
 producto = {"tomate":20000,"cebolla":30000,"ajos":15000}

 articulo = input("Ingrese el producto a buscar: ")
 if (producto.get(articulo)):
    print("El articulo si se encuentra")
 else:
   print("El articulo no se encuentra en el mercado")







if __name__=="__main__":
    main()