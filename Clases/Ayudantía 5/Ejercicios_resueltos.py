def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n-1)

def suma_digitos(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) + suma_digitos(n[1:])

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def invertir_cadena(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + invertir_cadena(s[:-1])

def contar_ceros(lista):
    if not lista:
        return 0
    else:
        return (1 if lista[0] == 0 else 0) + contar_ceros(lista[1:])

def contar_caminos(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return contar_caminos(m - 1, n) + contar_caminos(m, n - 1)
    
def buscar_numero(lista, x):
    if not lista:
        return False
    if lista[0] == x:
        return True
    return buscar_numero(lista[1:], x)

def contar_caracter(s, c):
    if not s:
        return 0
    else:
        return (1 if s[0] == c else 0) + contar_caracter(s[1:], c)


def torres_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        return print(f"Mover disco 1 desde {origen} hasta {destino}")
    else:
        torres_hanoi(n - 1, origen, destino, auxiliar)
        print(f"Mover disco {n} desde {origen} hasta {destino}")
        torres_hanoi(n - 1, auxiliar, origen, destino)



#print(potencia(2, 3))
#print(suma_digitos(1234))
#print(fibonacci(8))
#print(invertir_cadena("recursión"))
#print(contar_ceros([0, 1, 0, 2, 0, 3, 4]))
#print(contar_caminos(2, 2))
#print(buscar_numero([1, 2, 3, 4, 5], 3))
#print(contar_caracter("banana", "a"))
#torres_hanoi(10, 'A', 'B', 'C')