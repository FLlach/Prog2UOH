def invertir_orden_palabras(x):
    palabras = x.split()
    palabras_orden_invertido = palabras[::-1]
    return ' '.join(palabras_orden_invertido)

x = "hola mundo"
print(invertir_orden_palabras(x))
