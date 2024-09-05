import tkinter as tk

def habilitar_boton():
    if var.get() == 1:
        boton.config(state=tk.NORMAL)
    else:
        boton.config(state=tk.DISABLED)

ventana = tk.Tk()
ventana.title("Ejercicio 6")

var = tk.IntVar()

check = tk.Checkbutton(ventana, text="Habilitar botón", variable=var, command=habilitar_boton)
check.pack(pady=10)

boton = tk.Button(ventana, text="Enviar", state=tk.DISABLED)
boton.pack(pady=10)

ventana.mainloop()
