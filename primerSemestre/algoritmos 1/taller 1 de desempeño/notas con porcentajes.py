print("**COLEGIO EL ESTUDIANTE MENOS INTELIGENTE**")
print("--Deseo saber la nota final de mi semestre--")
print("Favor ingresa las 5 notas de la siguiente manera: 5.0, 4.3")
n1=float(input("Ingrese la nota del taller 1: "))
t1=n1*.20
n2=float(input("Ingrese la nota del taller 2: "))
t2=n2*.15
n3=float(input("Ingrese la nota del cuestionario 1: "))
t3=n3*.22
n4=float(input("Ingrese la nota del cuestionario 2: "))
t4=n4*.1
n5=float(input("Ingrese la nota del proyecto final: "))
t5=n5*.33
nd=t1+t2+t3+t4+t5
print(f'La nota definitiva del semestre es: {nd}')