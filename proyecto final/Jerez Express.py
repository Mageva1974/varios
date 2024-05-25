import tkinter as tk

jerez = tk.Tk()
jerez.title("JEREZ EXPRESS")

jerez.minsize(250,200)
jerez.maxsize(1200,335)
jerez.iconbitmap("favicon.ico")
jerez. configure(bg = "darkgrey")

bienvenida = tk.Label(jerez,text="JEREZ EXPRESS",bg="DarkSlateBlue",fg="black",font=("Arial Bold", 30))
bienvenida.pack()
visitas = tk.Label(jerez,text="Control de Visitas",bg ="SlateGray",fg="black",font=("Arial Bold", 25))
visitas.pack()

btn = tk.Button(jerez,text="Nueva Visita",command="", fg="black", font=("Arial"),bg ="DarkSlateBlue")
btn.pack()
btn.place( x = 100, y =135, height=55, width=350)

btn1 = tk.Button(jerez,text="Eliminadas Visita",command="", fg="black", font=("Arial"),bg ="DarkSlateBlue")
btn1.pack()
btn1.place( x = 800, y =135, height=55, width=350)

btn2 = tk.Button(jerez,text="Visitas Realizadas",command="", fg="black", font=("Arial"),bg ="SlateGray")
btn2.pack()
btn2.place( x = 100, y =235, height=55, width=350)

btn3 = tk.Button(jerez,text="Informes",command="", fg="black", font=("Arial"),bg ="SlateGray")
btn3.pack()
btn3.place( x = 800, y =235, height=55, width=350)



jerez.mainloop()