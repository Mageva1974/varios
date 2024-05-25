import tkinter as tk

def saludar():
    etiqueta_saludo.config(text="¡Hola, mundo!")

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Mi Primera Aplicación Tkinter")

# Crear una etiqueta
etiqueta_saludo = tk.Label(ventana, text="¡Bienvenido!")
etiqueta_saludo.pack()

# Crear un botón
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack()



# Mostrar la ventana
ventana.mainloop()
