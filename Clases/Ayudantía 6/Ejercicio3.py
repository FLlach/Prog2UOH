def potencia(x, n):
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if n == 0:
        return 1
    # Divide el exponente
    mitad = potencia(x, n // 2)
    # Si n es par, multiplicamos las dos mitades; si es impar, multiplicamos también por x
    if n % 2 == 0:
        return mitad * mitad
    else:
        return x * mitad * mitad


print(potencia(2, 10))
