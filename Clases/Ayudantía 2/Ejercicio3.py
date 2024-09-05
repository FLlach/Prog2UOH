import tkinter as tk

def mostrar_nombre():
    nombre = entrada.get()
    label_resultado.config(text=f"Hola, {nombre}!")

ventana = tk.Tk()
ventana.title("Ejercicio 3")

tk.Label(ventana, text="Nombre:", font=("Arial", 12, "bold")).pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Enviar", command=mostrar_nombre)
boton.pack(pady=10)

label_resultado = tk.Label(ventana, font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

ventana.mainloop()
