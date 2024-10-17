def quick_sort(arr):
    # Caso base: si el arreglo tiene uno o ningún elemento, ya está ordenado
    if len(arr) <= 1:
        return arr
    # Elegir el pivote
    pivote = arr[len(arr) // 2]
    # Dividir el arreglo en tres partes: menores, iguales, mayores
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    # Llamada recursiva y combinación de resultados
    return quick_sort(menores) + iguales + quick_sort(mayores)


arr = [5, 3, 8, 4, 2, 7, 6, 1]
print(quick_sort(arr))
