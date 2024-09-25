# Complejidad Algorítmica
### Conceptos Básicos
La mayoría de los problemas pueden ser solucionados usando diferentes algoritmos, lenguajes de programación e infraestructuras. Para comparar algoritmos, no se mide el tiempo de ejecución, sino la cantidad de Operaciones Elementales (OE) que realiza el algoritmo.

### Operaciones Elementales
Las OE son aquellas que el ordenador realiza en tiempo acotado por una constante. Ejemplos:

- Operaciones aritméticas y lógicas básicas.
- Asignaciones a variables escalares.
- Llamados y retornos de funciones.
- Tiempo de Ejecución
- El tiempo de ejecución de un algoritmo se denota con la letra 𝑇
- T, que indica la cantidad de OE en función del tamaño de la entrada.

Ejemplos de Complejidad:
$O(1)$: Operaciones constantes sin importar el tamaño de la entrada.
$O(n)$: Operaciones lineales que dependen directamente del tamaño de la entrada.
$O(log )(n)$: Complejidades logarítmicas que crecen más lentamente.

##### Problema: 
Imprime un triángulo rectángulo de 𝑁 filas compuesto por asteriscos.

```py
def print_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print("\n", end="")

```
Solución: La complejidad de este algoritmo es $𝑂(𝑛^2)$ debido a los bucles anidados.

# Notación Asintótica

La notación asintótica se utiliza para describir el comportamiento de un algoritmo a medida que el tamaño de entrada tiende a infinito.

Tipos de Notación:
O Grande (Big O): Da una cota superior al crecimiento del tiempo de ejecución.
$Ω$ (Omega): Da una cota inferior al crecimiento.
$Θ$ (Theta): Describe el crecimiento exacto.

Ejemplos de Crecimiento Asintótico:
$O(1)$: Operación constante.
$O(n)$: Crecimiento lineal.
$O(n^2)$: Crecimiento cuadrático.

##### Problema: 
Busca un número en una lista.

```py
def buscar(k, L):
    for i in range(len(L)):
        if k == L[i]:
            return i
    return None
```
Solución:

Mejor caso: $𝑂(1)$ si el elemento está al inicio de la lista.
Peor caso: $𝑂(𝑛)$ si el elemento está al final o no está en la lista.

##### Problema: 
Sumar todos los números de una lista.
```py
def sumar(L):
    suma = 0
    for i in L:
        suma += i
    return suma
```

### Propiedades de la Notación Asintótica

**Regla de la Suma**: Si un algoritmo tiene varias partes, la complejidad es la mayor de todas.
**Regla del Producto**: Si un algoritmo tiene bucles anidados, la complejidad es el producto de las complejidades de cada bucle.    


## Ejercicios propuestos

#### Buscar el Mínimo en una Lista
Escriba un algoritmo que encuentre el valor mínimo en una lista de números enteros.

```py
def encontrar_minimo(L):
    minimo = L[0]
    for i in L:
        if i < minimo:
            minimo = i
    return minimo
```
<details>
<summary>Respuesta</summary>

Complejidad: $O(n)$, ya que el algoritmo recorre la lista una vez.

</details>

#### Búsqueda Binaria
Implemente la búsqueda binaria en una lista ordenada para buscar un número específico.

```py
def busqueda_binaria(L, x):
    inicio = 0
    fin = len(L) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if L[medio] == x:
            return medio
        elif L[medio] < x:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
```
<details>
<summary>Respuesta</summary>

Complejidad: $O(log (n))$, gracias a la división del rango de búsqueda en cada iteración.

</details>

#### Multiplicación de Matrices
Multiplica dos matrices 𝐴 y 𝐵 y devuelve la matriz resultante.
```py
def multiplicar_matrices(A, B):
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado
```
<details>
<summary>Respuesta</summary>

Complejidad: $O(n^3)$ debido a los tres bucles anidados.

</details>

#### Fusión de Dos Listas Ordenadas
Fusiona dos listas ordenadas en una sola lista ordenada.

```py
def fusionar_listas(L1, L2):
    i, j = 0, 0
    resultado = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            resultado.append(L1[i])
            i += 1
        else:
            resultado.append(L2[j])
            j += 1
    resultado.extend(L1[i:])
    resultado.extend(L2[j:])
    return resultado
```

<details>
<summary>Respuesta</summary>

Complejidad: $O(n+m)$, donde n y m son las longitudes de las listas.

</details>

### Calcular la Serie de Fibonacci Iterativamente
Calcula la serie de Fibonacci hasta el n-ésimo término de manera iterativa.
```py
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```


<details>
<summary>Respuesta</summary>

Complejidad: $O(n)$.

</details>


### Generar Todas las Permutaciones de una Lista
Escriba una función que genere todas las permutaciones posibles de una lista de n elementos.

```py
def permutaciones(L):
    if len(L) == 0:
        return [[]]
    resultado = []
    for i in range(len(L)):
        # Extraer el elemento actual
        elemento = L[i]
        # Generar el resto de la lista excluyendo el elemento actual
        restante = L[:i] + L[i+1:]
        # Generar todas las permutaciones del resto y añadir el elemento actual a cada una
        for p in permutaciones(restante):
            resultado.append([elemento] + p)
    return resultado

# Ejemplo de uso
L = [1, 2, 3]
print(permutaciones(L))
```

<details>
<summary>Respuesta</summary>

Cálculo de Complejidad: O(n!)
Para entender por qué la complejidad es $O(n!)$, analicemos cómo el algoritmo trabaja recursivamente:

##### Número de llamadas recursivas:

En cada nivel de recursión, el algoritmo selecciona un elemento y llama recursivamente con el subconjunto restante.

Para una lista de tamaño n, se realizan n llamadas recursivas en el primer nivel, $(n−1)$ llamadas en el siguiente nivel, y así sucesivamente, hasta llegar a un caso base donde el subconjunto tiene tamaño 1.

##### Crecimiento Factorial:

El total de permutaciones posibles para n elementos es $n!$. Esto se debe a que en el primer nivel hay n opciones de selección, en el siguiente hay $(n−1)$, y así sucesivamente.
Por ejemplo, para $n=3$, el cálculo sería $3×2×1=6$.

###### Operaciones por cada permutación:
Para cada permutación, se realiza un número constante de operaciones (selección y concatenación), lo que no afecta significativamente la complejidad en comparación con el número de permutaciones generadas.

Por lo tanto, el costo total es proporcional al número de permutaciones generadas, es decir, $O(n!)$.

</details>