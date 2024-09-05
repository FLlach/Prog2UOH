import tkinter as tk

def calcular(operacion):
    numeros = entrada.get().split()
    if len(numeros) == 2:
        num1, num2 = float(numeros[0]), float(numeros[1])
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2
        label_resultado.config(text=f"Resultado: {resultado}")
    else:
        label_resultado.config(text="Por favor, ingrese dos números separados por espacio.")

ventana = tk.Tk()
ventana.title("Ejercicio 9")

tk.Label(ventana, text="Ingrese dos números:").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="+", command=lambda: calcular("+")).pack(side=tk.LEFT, padx=5)
tk.Button(ventana, text="-", command=lambda: calcular("-")).pack(side=tk.LEFT, padx=5)
tk.Button(ventana, text="*", command=lambda: calcular("*")).pack(side=tk.LEFT, padx=5)
tk.Button(ventana, text="/", command=lambda: calcular("/")).pack(side=tk.LEFT, padx=5)

label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=10)

ventana.mainloop()
