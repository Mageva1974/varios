print("Colegio el desaplicado")
print("Vamos a calcular el promedio de notas de un alunmo\n")
nota1=float(input("Ingrese la nota 1: "))
nota2=float(input("Ingrese la nota 2: "))
nota3=float(input("Ingrese la nota 3: "))
nota4=float(input("Ingrese la nota 4:"))
nota5=float(input("Ingrese la nota 5: "))
promedio=(nota1+nota2+nota3+nota4+nota5)/5
if promedio<5:
    print("El alumno reprobo el curso")
else:
    print("El alumno aprobó el curso")

