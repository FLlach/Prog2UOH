import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 1")

label = tk.Label(ventana, text="Bienvenido a Tkinter", bg="blue", fg="white", font=("Arial", 20, "bold"))
label.pack(padx=20, pady=20)

ventana.mainloop()
