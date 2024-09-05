import tkinter as tk
from tkinter import ttk

def iniciar_proceso():
    progress.start(10)

ventana = tk.Tk()
ventana.title("Ejercicio 8")

progress = ttk.Progressbar(ventana, length=200, mode='determinate')
progress.pack(pady=20)

boton = tk.Button(ventana, text="Iniciar Proceso", command=iniciar_proceso)
boton.pack(pady=10)

ventana.mainloop()
