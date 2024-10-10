# Recursividad
La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver subproblemas del problema original.

### ¿Qué es la Recursividad?
Recursividad significa que una función realiza llamadas a sí misma en su propia definición. La idea es que un problema grande se puede dividir en subproblemas más pequeños, cada uno de los cuales se puede resolver con la misma técnica que el problema original. Cuando la función se llama a sí misma, se va resolviendo cada subproblema hasta alcanzar un caso base.

![Alt text](recursion_meme.webp)

### Componentes de la Recursividad
Para que una función recursiva funcione correctamente, debe incluir dos componentes clave:


- Caso Base:

    - Es la condición que detiene las llamadas recursivas. Es fundamental, ya que sin este caso, la función continuaría llamándose a sí misma de manera indefinida, resultando en un desbordamiento de pila (stack overflow).

    - El caso base generalmente se diseña para manejar la entrada más pequeña o trivial del problema.

- Llamada Recursiva:

    - Es la parte de la función que resuelve una parte del problema y luego llama a la función nuevamente con un subproblema más pequeño o más simple.

    - Cada llamada recursiva se aproxima al caso base, de modo que eventualmente la función lo alcanzará y se detendrá.

### Ejemplo:  Factorial

El cálculo del factorial de un número n.
Por definición el factorial de un número se define como el producto de todos los números enteros positivos hasta ese número. 
Por definición matemática de factorial:

$n! =n×(n−1)!$
$0! =1$

```py
def factorial(n):
    # Caso Base
    if n == 0:
        return 1
    # Llamada Recursiva
    else:
        return n * factorial(n - 1)
```

<details>
<summary>Explicación</summary>

- Caso Base: Cuando $n=0$, devuelve $1$.

- Llamada Recursiva: Se llama a la función con $n−1$, resolviendo gradualmente el problema.


</details>

## Tipos de Recursividad

Existen multiples tipos de recursividad que pueden aplicarse en función del diseño del problema:

#### Recursividad Simple:

Una función se llama a sí misma una sola vez. 

El ejemplo del factorial es una recursión simple.

#### Recursividad Múltiple:

Una función se llama a sí misma más de una vez en su definición. 
Un ejemplo clásico: **Fibonacci**.


```py
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
#### Recursividad Anidada:

Una función recursiva se utiliza como un argumento para otra llamada recursiva. Este tipo es menos común y puede ser más difícil de leer.

#### Recursividad de Cola (Tail Recursion):

La última operación de la función es la llamada recursiva. En algunos lenguajes, esto permite optimizaciones que ahorran espacio en la pila de llamadas.

```py
def factorial_tail(n, acumulador=1):
    if n == 0:
        return acumulador
    else:
        return factorial_tail(n - 1, n * acumulador)
```
### Ventajas de la Recursividad

- Elegancia y Simplicidad: 
    - La recursión puede reducir un problema complejo a una definición más sencilla y clara.

- Solución Directa para Problemas Divisibles:
    - La recursión es ideal para problemas que se pueden dividir en subproblemas más pequeños, como algoritmos de búsqueda binaria, recorrido de árboles y gráficos.

- Reducción de Código: 
    - En algunos casos, la recursión permite escribir menos código en comparación con las soluciones iterativas.

## Desventajas de la Recursividad

- Uso de Memoria:
    - Las llamadas recursivas ocupan espacio en la pila de llamadas, lo que puede llevar a un desbordamiento si la recursión es demasiado profunda.

- Rendimiento: 
    - La recursión a menudo es menos eficiente que las soluciones iterativas. Por ejemplo, el cálculo de Fibonacci es ineficiente cuando se realiza de manera recursiva sin optimización.

- Complejidad de Depuración: 
    -Los errores en funciones recursivas pueden ser difíciles de rastrear y depurar debido a la naturaleza repetitiva de las llamadas a funciones.

Ejemplo Avanzado: Recorrido en Árboles Binarios

El recorrido en un árbol binario es un ejemplo común de recursión en estructuras de datos. Supongamos que queremos recorrer un árbol en orden (izquierda, raíz, derecha).

```py
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def recorrido_enorden(nodo):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda)
        print(nodo.valor)
        recorrido_inorden(nodo.derecha)
```
<details>
<summary>Explicación</summary>

La función ```recorrido_enorden``` se llama a sí misma para recorrer primero el subárbol izquierdo, luego visita el nodo raíz y, finalmente, el subárbol derecho.

Cada nodo se visita exactamente una vez, por lo que la complejidad es 
$O(n)$, siendo $n$ el número de nodos en el árbol.

</details>


### ¿Cuándo Usar Recursión?
La recursión es especialmente útil para:

- Problemas con una estructura fractal, como gráficos y árboles.

- Problemas que se resuelven de manera natural dividiéndolos en subproblemas similares.

- Algoritmos de retroceso (backtracking), como en el caso del problema de las n-reinas, generación de permutaciones o combinaciones.

## Ejercicios propuestos:
_(La plantilla se encuentra en el repositorio)_

1) Implemente una función recursiva que calcule la potencia de un número x elevado a n.

```py
def potencia(x, n):
    
```
2) Escriba una función recursiva que calcule la suma de los dígitos de un número entero positivo.

```py
def suma_digitos(n):

```

3) Implemente una función recursiva para calcular el n-ésimo número de la serie de Fibonacci.

```py
def fibonacci(n):

```

4) Cree una función recursiva que invierta una cadena de caracteres.

```py
def invertir_cadena(s):

```
5)  Escribe una función recursiva que cuente el número de ceros en una lista de enteros.

```py
def contar_ceros(lista):

```
6) Dada una cuadrícula de m×n en la que solo pueden moverte hacia abajo o hacia la derecha. Escribe una función recursiva para contar cuántos caminos diferentes hay desde la esquina superior izquierda hasta la esquina inferior derecha.

```py
def contar_caminos(m, n):

```

7) Escriba una función recursiva que busque un número en una lista. Si el número está en la lista, devuelve ```True```; de lo contrario, devuelve ```False```.

```py
def buscar_numero(lista, x):

```

```py
def contar_caracter(s, c):

```

8) Resuelva el problema de las Torres de Hanói. Escribe una función recursiva que muestre los movimientos necesarios para trasladar $n$ discos desde el origen hasta el destino usando un poste auxiliar.

```py
def torres_hanoi(n, origen, auxiliar, destino):

```

![Alt text](hanoi_algorithm.png)
