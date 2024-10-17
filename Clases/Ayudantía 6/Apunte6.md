# Divide & Conquer
Enfoque fundamental en programación que se utiliza para resolver problemas complejos de manera más eficiente.

La idea es dividir el problema original en subproblemas más pequeños, resolver cada uno de estos subproblemas de forma recursiva y luego combinar las soluciones parciales para obtener la solución final.

### Pasos del Enfoque Divide y Vencerás

- Dividir (Divide):

    - El problema original se descompone en uno o más subproblemas más pequeños, similares al problema original pero de menor tamaño.
    Estos subproblemas deben ser más simples o menores, lo que permitirá abordar el problema general de forma recursiva.

- Resolver (Conquer):

    - Se resuelven los subproblemas de forma recursiva.
    Si el subproblema es lo suficientemente simple (es decir, alcanza un caso base), se resuelve directamente.
    A menudo, esto implica una llamada recursiva para descomponer el problema aún más hasta que alcance el caso base.

- Combinar (Combine):

    - Las soluciones a los subproblemas se combinan para formar la solución al problema original.
    El paso de combinación suele implicar una operación para juntar o procesar las respuestas de cada subproblema resuelto.

### Ejemplos Comunes

#### Merge Sort (Ordenamiento por Mezcla):

**Divide**: Divide la lista en dos mitades.
**Conquer**: Ordena recursivamente cada mitad.
**Combine**: Fusiona las dos mitades ordenadas para obtener una lista ordenada.
**Complejidad**: $O(n log(n))$.

#### Quick Sort (Ordenamiento Rápido):

**Divide**: Selecciona un elemento como pivote y divide la lista en dos sublistas: una con elementos menores al pivote y otra con elementos mayores.
**Conquer**: Ordena recursivamente cada sublista.
**Combine**: Como cada sublista se ordena en su lugar, la combinación ya se da naturalmente.
**Complejidad**: $O(nlog(n))$ en promedio.

#### Búsqueda Binaria:

**Divide**: Divide una lista ordenada a la mitad y determina si el elemento buscado está en la mitad izquierda o derecha.

    
**Conquer**: Realiza la búsqueda en la mitad relevante.
**Combine**: No es necesario un paso de combinación; el elemento se encuentra o se confirma que no está presente.
**Complejidad**: $O(log n)$.

### Ventajas

**Eficiencia en Tiempo**: Muchos algoritmos de ordenamiento y búsqueda que usan Divide y Vencerás tienen complejidad $O(nlog(n))$, mucho más rápida que $O(n^2)$ de métodos iterativos simples.

**Uso de Recursión**: Este enfoque es particularmente adecuado para la recursión, lo que hace que el código sea más conciso y expresivo.

**Aplicabilidad en Problemas Complejos**: Divide y Vencerás es muy útil para problemas que tienen una estructura fractal o se pueden dividir en partes similares al problema original, como gráficos, árboles y matrices.

**Paralelización**: Dado que los subproblemas son independientes, es posible ejecutar el enfoque de manera concurrente o paralela, lo que permite aprovechar mejor los sistemas multiprocesadores.

### Desventajas 

**Uso de Memoria**: La recursión y la necesidad de almacenar los subproblemas y sus soluciones pueden llevar a un mayor consumo de memoria.

**Coste de Combinación**: En algunos casos, el paso de combinación puede ser costoso en términos de tiempo y espacio. Por ejemplo, en Merge Sort, la combinación de dos listas ordenadas requiere un espacio adicional proporcional al tamaño de las listas.

**Recursión Ineficiente en Algunos Casos**: La recursión puede no ser la mejor opción para problemas que no se dividen fácilmente en subproblemas o cuando el coste de la división y combinación supera los beneficios.

## Ejercicios

1) Escribe una función recursiva que encuentre el valor máximo en un arreglo de números utilizando Divide & Conquer.

2) Implementa el algoritmo de Merge Sort para ordenar una lista de números.

3) Escribe una función recursiva para calcular $x^n$ utilizando Divide y Vencerás, donde n es un número entero positivo.

4) Implementa el algoritmo de Quick sorting