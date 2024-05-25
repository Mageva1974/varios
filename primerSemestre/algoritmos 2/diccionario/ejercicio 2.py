#auto = {"chevrolet": "spark", "mazda": "miata", "renault": "logan"}

#print(auto)
#-------------------------------------------------------------
  # para acceder un directorio
#print(auto["mazda"])
#-------------------------------------------------------------
  #para modificar un directorio
#auto["renault"] = "megane"
#print(auto)
#-------------------------------------------------------------
  #imprime los key(atributos)del diccionario
#for x in auto:
#    print(x)
#-------------------------------------------------------------
   #imprime los values(valor) solamente
#for x in auto:
#    print(auto[x])
#-------------------------------------------------------------
   #imprime los key y values con simbolos
#for clave,values in auto.items():
#    print(clave,"*",values)
#    print(clave, "/", values)
#-----------------------------------------------------------------
  #para unir dos diccionarios
auto = {"chevrolet": "spark", "mazda": "miata", "renault": "logan"}
auto2 = {"audi": "a4", "bmw": "m3", "toyota": "4runner","mini": "paceman"}
#autos ={ "auto":auto,
#        "auto2":auto2}
#print(autos)
#---------------------------------------------------------------------------
  #para eliminar un registro del diccionario
#auto.clear()
#print(auto)
#---------------------------------------------------------------------------
  #permite consultar un registro y sino se encuentra no aparece error
#print(auto.get("mazda"))
#print(auto.get("p3","no encontrado"))
#--------------------------------------------------------------------------------
   #devuelve una lista con todos los keys
#j = auto.keys()
#print(j)
#print(list(j))
#----------------------------------------------------------------
   #devuelve los values de un directorio
#print(list(auto.values()))
#--------------------------------------------------------------------------------
    #elinina un values deterninado
#auto.pop("chevrolet")
#print(auto)
#--------------------------------------------------------------------------------
   #elinina de forma aleatoria un elemento del diccionario
#auto.popitem()
#print(auto)
#--------------------------------------------------------------------------------
   #actuliza un elemento del diccionario
auto.update(auto2)
print(auto)

