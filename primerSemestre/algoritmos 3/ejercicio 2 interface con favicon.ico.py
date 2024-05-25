import tkinter as tk
jerez = tk.Tk()
jerez.title("Alimentos Saludables")

#jerez.geometry("300x500")
jerez.minsize(250,200)
jerez.maxsize(1200,300)
jerez.iconbitmap("favicon.ico")
jerez.configure(bg ="darkgrey")

bienvenida = tk.Label(jerez,text="BIENVENIDO",bg="red",fg="black",font=("Arial Bold", 40))
bienvenida.pack()

def saludo():
    tk.Label(jerez,text="hola sapos").pack()

btn = tk.Button(jerez,text="INGRESO",command=saludo, fg="black", font=("Arial"))
btn.pack()
btn.place( x = 500, y = 90, height=175, width=150)

jerez.mainloop()


