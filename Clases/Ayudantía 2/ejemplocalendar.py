import tkinter as tk
from tkcalendar import DateEntry

def mostrar_fecha():
    fecha = calendar.get_date()
    label_fecha.config(text=f"Fecha seleccionada: {fecha}")

ventana = tk.Tk()
ventana.title("Ejercicio tkcalendar")

# Crear un DateEntry para seleccionar una fecha
calendar = DateEntry(ventana, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
calendar.pack(pady=20)

# Botón para mostrar la fecha seleccionada
boton = tk.Button(ventana, text="Mostrar Fecha", command=mostrar_fecha)
boton.pack(pady=10)

# Label para mostrar la fecha seleccionada
label_fecha = tk.Label(ventana, text="")
label_fecha.pack(pady=10)

ventana.mainloop()
