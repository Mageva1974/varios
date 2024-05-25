
def main():
 print(" * * MERCADO EL CENTAVO FALSO * * ")
 producto = {}
 cant =int(input("Favor indicar la cantidad de productos a ingresar: "))
 for i in range(0, cant):
         clave = input("Ingrese el nombre del producto {}: ".format(i + 1))
         valor = input("Ingrese el valor del producto {}: ".format(i + 1))
         producto[clave] = valor
 print("El mercado es:", producto)

 for i in range(0,cant):
  articulo = input("Ingrese el producto a buscar: ")
  if (producto.get(articulo)):
    print("El precio del articulo es: ", producto[articulo])
  else:
    print("El articulo no se encuentra en el mercado")
  break




 """for i in range(0, cant):
  producto[input("Ingrese el nombre del producto: ")] = float(input("Ingrese el precio del producto: "))
  print(producto)"""

if __name__=="__main__":
    main()