print("CENTRO DE LLAMADAS AL GRATIN")
usa=900
canada=800
euro=950
resto=1250


print("FAVOR INGRESAR EL DESTINO DE LA LLAMADA ASI: ")
print("Si es a Estados Unidos en destino debe escribir: usa")
print("Si es a Canada en destino debe escribir: canada")
print("Si es a Europa en destino debe escribir: euro")
print("Si es a el Resto del mundo en destino debe escribir: resto")
print("****************************************************************")
destino=input("Ingrese el destino de la llamada:")
tiempo=int(input("Favor ingresar el tiempo de la llamada:"))

if (destino=="usa"):
    if(destino=="usa"and tiempo>15):
        valor=float((usa*tiempo)-((usa*tiempo)*.20))
        print(f"el valor de la llamada es: {valor}")
    else:
        valor=float(usa*tiempo)
        print(f"el valor de la llamada es: {valor}")

if (destino=="canada"):
    if(destino=="canada"and tiempo>15):
        valor=float((canada*tiempo)-((canada*tiempo)*.20))
        print(f"el valor de la llamada es: {valor}")
    else:
        valor=float(canada*tiempo)
        print(f"el valor de la llamada es: {valor}")


if (destino=="euro"):
    if(destino=="euro"and tiempo>15):
        valor=float((euro*tiempo)-((euro*tiempo)*.20))
        print(f"el valor de la llamada es: {valor}")
    else:
        valor=float(euro*tiempo)
        print(f"el valor de la llamada es: {valor}")

if (destino=="resto"):
    if(destino=="resto"and tiempo>15):
        valor=float((resto*tiempo)-((resto*tiempo)*.20))
        print(f"el valor de la llamada es: {valor}")
    else:
        valor=float(resto*tiempo)
        print(f"el valor de la llamada es: {valor}")






