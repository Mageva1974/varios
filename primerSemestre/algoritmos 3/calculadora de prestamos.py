import math
def mensual(cant, tiempo, interes):
   int_men = (interes/12)/100
   cuota = ((cant * int_men)/(1-(1+int_men)**(tiempo*(-1))))
   return cuota

def main():
    print("** PRESTAMOS EL QUE NO TIENE NADA")
    print("=========================================================")
    cant =float( input("Favor ingresar la cantidad del pestamo: "))
    tiempo =int(input("Favor ingresar el tiempo al que desea pagar el prestamo en meses 12, 24, 36 : "))
    interes = float(input("favor ingresar el interes anual para el prestamo: "))
    cuota = float(mensual(cant, tiempo, interes))
    int_men = (interes / 12) / 100
    print("")
    print("\t\t Prestamo")
    print("-------------------------------------------------------------")
    print(f"Valor del Prestamo: {cant:.2f};\t\t Interes anual: {interes} %")
    print(f"Plazo del pretamo: {tiempo:.0f}")
    print("")
    print("{:^10}{:^16}{:^10}{:^10}{:^10}".format("N°", "Cuota",  "int_men", " Amortizacion", " Saldo"))
    nue_sal = cant
    for i in range(tiempo+1):
        if(i == 0):
            print("{:^10}{:^10}{:^10}{:^15}{:^10}".format(i, "-", "-", "-", cant))
        else:
            pag_men = nue_sal * int_men
            Amotizacion = cuota - pag_men
            nue_sal = nue_sal - Amotizacion
            print("{:^10d}{:^14.2f}{:^10.2f}{:^15.2f}{:^14.2f}".format(i, cuota, pag_men, Amotizacion, nue_sal))




if __name__=="__main__":
    main()









