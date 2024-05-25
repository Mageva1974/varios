
def main():
 print("UNIVERSIDAD EL SABELOTODO")
 asignatura = ["Español", "Matematicas", "Ingles", "Ciencias", "Filosofia", "Quimica"]
 nota =[]
 for i in range(6):
     print(f"favor ingresar la nota de {asignatura[i]}: ")
     notas=input("ingrese la nota ")
     nota.append(notas)

 for i in range(6):
     print(f"En {asignatura[i]} usted a sacado la nota : {nota[i]} ")

if __name__=="__main__":
    main()
