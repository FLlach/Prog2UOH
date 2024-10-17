def merge_sort(arr):
    # Caso base: si el arreglo tiene un solo elemento o está vacío
    if len(arr) <= 1:
        return arr
    # Divide el arreglo en dos mitades
    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])
    # Combina ambas mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    # Compara y mezcla los elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    # Agrega los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


arr = [5, 3, 8, 6, 2, 7]
print(merge_sort(arr))
