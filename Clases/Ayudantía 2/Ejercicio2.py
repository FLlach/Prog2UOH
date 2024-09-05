import tkinter as tk

def boton_presionado():
    boton.config(text="¡Has presionado el botón!", bg="red")

ventana = tk.Tk()
ventana.title("Ejercicio 2")

boton = tk.Button(ventana, text="Presiona aquí", command=boton_presionado)
boton.pack(padx=20, pady=20)

ventana.mainloop()