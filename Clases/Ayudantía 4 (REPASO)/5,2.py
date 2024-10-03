def invertir_palabras(x):
    palabras = x.split()
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    return ' '.join(palabras_invertidas)

x = "hola mundo"
print(invertir_palabras(x)) 
