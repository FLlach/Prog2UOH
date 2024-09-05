import tkinter as tk

def hover_boton1(event):
    boton1.config(bg="green")

def salir_boton1(event):
    boton1.config(bg="SystemButtonFace")

def hover_boton2(event):
    boton2.config(bg="yellow")

def salir_boton2(event):
    boton2.config(bg="SystemButtonFace")

ventana = tk.Tk()
ventana.title("Ejercicio 4")

boton1 = tk.Button(ventana, text="Botón 1")
boton1.pack(padx=20, pady=10)
boton1.bind("<Enter>", hover_boton1)
boton1.bind("<Leave>", salir_boton1)

boton2 = tk.Button(ventana, text="Botón 2")
boton2.pack(padx=20, pady=10)
boton2.bind("<Enter>", hover_boton2)
boton2.bind("<Leave>", salir_boton2)

ventana.mainloop()
