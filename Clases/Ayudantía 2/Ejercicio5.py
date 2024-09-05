import tkinter as tk

def cambiar_color(color):
    label.config(bg=color)

ventana = tk.Tk()
ventana.title("Ejercicio 5")

label = tk.Label(ventana, text="Elige un color", bg="white", font=("Arial", 16))
label.pack(pady=20, padx=20)

boton_rojo = tk.Button(ventana, text="Rojo", command=lambda: cambiar_color("red"))
boton_rojo.pack(side=tk.LEFT, padx=10)

boton_verde = tk.Button(ventana, text="Verde", command=lambda: cambiar_color("green"))
boton_verde.pack(side=tk.LEFT, padx=10)

boton_azul = tk.Button(ventana, text="Azul", command=lambda: cambiar_color("blue"))
boton_azul.pack(side=tk.LEFT, padx=10)

ventana.mainloop()
