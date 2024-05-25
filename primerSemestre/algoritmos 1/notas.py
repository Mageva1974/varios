print("COLEGIO EL ESTUDIANTE MENOS PEOR")
print("El valor de la matricula para el proximo año es de 500.000")
nombre=input("Favor ingresar el nombre del estudiante:")
print(f"Favor ingresar las notas asi, ejemplo: 4.5")
n1=float(input("Favor ingresar la nota # 1:"))
n2=float(input("Favor ingresar la nota # 2:"))
n3=float(input("Favor ingresar la nota # 3:"))
n4=float(input("Favor ingresar la nota # 4:"))

promedio=(n1+n2+n3+n4)/4

if(promedio>=4):
    print("las notas del alumno son excelentes")
    matricula = 500000 - (500000 * .2)
    print(f"Por tal motivo el alumno tendra un descuento del 20% en su matricula")
    print('la matricula sera: {:,.0f}'.format(matricula))

if(promedio>=3 and promedio<4):
    print("las notas del alumno son buenas")

if(promedio<3):
    print("Las notas del alumno son deficientes")






