import tkinter as tk

def verificar_login():
    usuario = entrada_usuario.get()
    if not usuario:
        label_mensaje.config(text="El campo usuario no puede estar vacío", fg="red")
    else:
        label_mensaje.config(text=f"Bienvenido, {usuario}!", fg="green")

ventana = tk.Tk()
ventana.title("Ejercicio 7")

tk.Label(ventana, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entrada_password = tk.Entry(ventana, show="*")
entrada_password.pack(pady=5)

boton_login = tk.Button(ventana, text="Login", command=verificar_login)
boton_login.pack(pady=10)

label_mensaje = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
label_mensaje.pack(pady=10)

ventana.mainloop()
