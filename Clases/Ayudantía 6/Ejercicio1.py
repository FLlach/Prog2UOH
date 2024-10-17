def maximo_arreglo(arr):
    # Caso base: si el arreglo tiene un solo elemento
    if len(arr) == 1:
        return arr[0]
    # Divide el arreglo en dos mitades
    mid = len(arr) // 2
    # Llamada recursiva para encontrar el máximo en ambas mitades
    max_izq = maximo_arreglo(arr[:mid])
    max_der = maximo_arreglo(arr[mid:])
    # Combina los resultados encontrando el máximo entre ambos
    return max(max_izq, max_der)


arr = [1, 5, 3, 9, 2]
print(maximo_arreglo(arr)) 
