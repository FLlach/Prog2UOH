# Ayudantía 1
## Paradigmas de programación
Los paradigmas de programación son enfoques o estilos metodológicos que guían la forma en que se estructura y organiza el código para resolver problemas específicos en el desarrollo de software. Cada paradigma ofrece un marco conceptual diferente para abordar tareas de programación, facilitando la resolución de ciertos tipos de problemas al proporcionar herramientas y técnicas adaptadas a esas necesidades.

---

### Programación Imperativa:
Este paradigma se centra en describir cómo se debe realizar una tarea mediante instrucciones secuenciales. Los lenguajes como C, C++, y Python pueden ser utilizados de manera imperativa. Se enfoca en modificar el estado del programa mediante la asignación de variables y el uso de estructuras de control como bucles y condicionales.
```py
# Ejemplo imperativo: calcular la suma de los primeros 5 números
suma = 0
for i in range(1, 6):
    suma += i
print(suma)  # Salida: 15

```

---

### Programación Orientada a Objetos (POO): 
Este paradigma organiza el software en objetos que representan entidades del mundo real o conceptos abstractos. Cada objeto contiene datos (atributos) y métodos (funciones) que operan sobre los datos. La POO facilita la reutilización de código y la modularidad. Lenguajes como Java, C++, Python y C# son ampliamente utilizados en este paradigma.
```py
# Ejemplo de POO: clase simple que representa un Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

# Crear un objeto de la clase Circulo
mi_circulo = Circulo(5)
print(mi_circulo.calcular_area())  # Salida: 78.53975


```

---

### Programación Funcional:
Se basa en el uso de funciones matemáticas puras y evita el estado mutable y los efectos secundarios. En este paradigma, las funciones son "ciudadanas de primera clase", lo que significa que pueden ser pasadas como argumentos, retornadas por otras funciones y asignadas a variables. Ejemplos de lenguajes funcionales incluyen Haskell, Lisp y, en menor medida, Python y JavaScript.
```py
from functools import reduce

# Ejemplo funcional: calcular el factorial de un número
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(5))  # Salida: 120


```
---

### Programación Lógica: 
Se basa en la lógica formal, utilizando reglas y hechos para derivar conclusiones. En este paradigma, el programador define "qué" es el problema y las relaciones entre los datos, mientras que el motor de inferencia del lenguaje determina "cómo" resolver el problema. Prolog es uno de los lenguajes más conocidos en este paradigma.
```py
# Ejemplo lógico: demostrar lógica con pyDatalog
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, amigo')

# Definimos relaciones
+ amigo('Juan', 'Maria')
+ amigo('Maria', 'Pedro')
+ amigo('Pedro', 'Juan')

# Consulta de relación
print(amigo(X, 'Maria'))  # Salida: X = Juan
```
---

### Programación Declarativa:
Se centra en describir qué debe hacer el programa sin especificar cómo hacerlo. Los lenguajes declarativos incluyen SQL para bases de datos y HTML para el marcado de páginas web. Este paradigma contrasta con el imperativo en que no especifica un control de flujo detallado.
```py
# Ejemplo declarativo: obtener números pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # Salida: [2, 4, 6]

```
---

### Programación Reactiva: 
Se centra en flujos de datos y la propagación de cambios. Es útil para aplicaciones que requieren una alta capacidad de respuesta a eventos, como interfaces de usuario interactivas o sistemas de tiempo real. Este paradigma utiliza conceptos como observables y suscripciones. Frameworks y bibliotecas como RxJS en JavaScript son ejemplos de este paradigma.
```py
from rx import from_list
from rx.operators import filter, map

# Ejemplo reactivo: flujo de datos para filtrar y transformar
numeros = from_list([1, 2, 3, 4, 5, 6])
numeros.pipe(
    filter(lambda n: n % 2 == 0),
    map(lambda n: n * n)
).subscribe(lambda x: print(x))  # Salida: 4, 16, 36
```
---

## Programación Orientada a Objetos

POO se enfoca principalmente en dos conceptos angulares: 

Clase: Es un modelo o plantilla que define una estructura de datos y los comportamientos asociados a esos datos. Una clase puede contener atributos (variables) y métodos (funciones).

Objeto: Es una instancia de una clase. Cuando creas un objeto, estás creando una instancia de la clase con valores específicos.

Dentro de las clases podemos encontrar diferentes conceptos:
- Atributos: Variables que pertenecen a cada instancia de la clase (es decir, a cada objeto). Se definen en el constructor `(__init__)`.

- Atributos de clase: Variables que son compartidas entre todas las instancias de la clase. Se definen directamente en la clase.

- Métodos: Funciones definidas dentro de una clase que describen los comportamientos que un objeto puede realizar. Los métodos de instancia toman self como su primer argumento, lo cual es una referencia al objeto actual.

Métodos Especiales: Python ofrece métodos especiales que tienen funciones específicas, como el constructor `__init__`, el método de representación `__str__`, y el método destructor `__del__`.

### Propiedades

#### Herencia 
La herencia es un mecanismo que permite crear nuevas clases (clases hijas) basadas en clases existentes (clases padres). Las clases hijas heredan atributos y métodos de las clases padres, lo que facilita la reutilización del código y la creación de relaciones jerárquicas entre clases.

- Ventajas:
    - Reutilización del código: Evita la duplicación de código al permitir que las clases hijas hereden funcionalidades de las clases padres.
    - Mantenimiento más sencillo: Cambios en la clase base se reflejan automáticamente en las clases derivadas.
    - Extensibilidad: Permite extender las funcionalidades de las clases existentes sin modificar el código original.

    ```py
    class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    class Perro(Animal):  # Perro hereda de Animal
        def hacer_sonido(self):
            return "Guau"

    class Gato(Animal):  # Gato hereda de Animal
        def hacer_sonido(self):
            return "Miau"

    perro = Perro("Firulais")
    gato = Gato("Michi")

    print(perro.hacer_sonido())  # Salida: Guau
    print(gato.hacer_sonido())   # Salida: Miau

    ```
---
#### Polimorfismo
El polimorfismo permite que una sola interfaz sea utilizada para representar diferentes tipos de objetos. En otras palabras, diferentes clases pueden ser tratadas como instancias de una clase base común, permitiendo que el mismo método pueda tener diferentes comportamientos dependiendo del objeto con el que se invoque.

- Ventajas:
    - Flexibilidad: Permite que el código trabaje con diferentes tipos de objetos sin necesidad de conocer sus diferencias internas.
    - Extensibilidad: Es fácil añadir nuevas clases que implementen métodos existentes.
    ```py
    class Animal:
    def hacer_sonido(self):
        pass

    class Perro(Animal):
        def hacer_sonido(self):
            return "Guau"

    class Gato(Animal):
        def hacer_sonido(self):
            return "Miau"

    # Polimorfismo: ambos objetos se tratan como instancias de la clase Animal
    animales = [Perro(), Gato()]

    for animal in animales:
        print(animal.hacer_sonido())  # Salida: Guau, Miau

    ```
---
#### Encapsulamiento
El encapsulamiento es el mecanismo que restringe el acceso directo a los atributos y métodos de un objeto, protegiendo así los datos internos del objeto y asegurando que solo se pueda acceder a ellos a través de métodos definidos. Esto asegura que los datos sean manipulados de manera controlada.

- Ventajas:
    - Protección de datos: Evita modificaciones no autorizadas o no intencionadas a los datos internos.
    - Modularidad: Mejora la modularidad al ocultar los detalles de implementación internos.
    - Mantenimiento: Facilita el mantenimiento del código al asegurar que los cambios en la implementación interna no afecten el código externo.
    ```py
    class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self.__saldo

    # Crear objeto
    cuenta = CuentaBancaria(1000)

    cuenta.depositar(500)
    cuenta.retirar(200)
    print(cuenta.obtener_saldo())  # Salida: 1300

    # print(cuenta.__saldo)  # Error: atributo privado no accesible directamente

    ```
---
#### Abstracción
La abstracción consiste en ocultar los detalles complejos de implementación y mostrar únicamente las funcionalidades esenciales de un objeto. Esto permite a los desarrolladores trabajar con conceptos a nivel de alto, sin preocuparse por los detalles internos de implementación.

- Ventajas:
    - Simplicidad: Hace que el código sea más simple y fácil de entender al ocultar los detalles internos.
    - Flexibilidad: Facilita la actualización o modificación del código sin afectar a los usuarios externos.
    - Mantenibilidad: Ayuda a mantener un código más claro y estructurado, lo que facilita su mantenimiento.

```py
from abc import ABC, abstractmethod

class Forma(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Crear objetos
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print(circulo.area())     # Salida: 78.53975
print(rectangulo.area())  # Salida: 24

```
---

