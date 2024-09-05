# Introducción a Tkinter en Python

`Tkinter` es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Ofrece un conjunto de widgets que permiten crear aplicaciones interactivas de manera simple.

https://docs.python.org/3/library/tkinter.html#module-tkinter

## Instalación 

No es necesario instalar `Tkinter`, ya que viene incluido en la distribución estándar, pero si se pueden instalar otras bibliotecas para usar dentro de Tkinter tal como `Tkcalendar` 

## Primeros pasos

Tkinter se usa mediante la inicialización de objetos, al instanciar la clase de tkinter como tk y de esta manera tenemos acceso a todos los métodos propios de la clase  

```py
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana con Tkinter")

# Etiqueta simple
etiqueta = tk.Label(ventana, text="¡Hola, Mundo!")
etiqueta.pack()

# Bucle principal
ventana.mainloop()
```

## Widgets
- ### Label
```py
label = tk.Label(ventana, text="Texto de ejemplo")
label.pack()
```
- ### Button
```py
def boton_click():
    print("Botón presionado")

boton = tk.Button(ventana, text="Presionar", command=boton_click)
boton.pack()
```
- ### Entry
```py
entrada = tk.Entry(ventana)
entrada.pack()
```
- ### Frame
```py
frame = tk.Frame(ventana)
frame.pack()

boton1 = tk.Button(frame, text="Botón 1")
boton1.pack(side=tk.LEFT)

boton2 = tk.Button(frame, text="Botón 2")
boton2.pack(side=tk.LEFT)
```
- ### Text
```py
texto = tk.Text(ventana, height=5, width=40)
texto.pack()
```
- ### Checkbutton
```py
var = tk.IntVar()
check = tk.Checkbutton(ventana, text="Opción 1", variable=var)
check.pack()
```
- ### Radiobutton
```py
opcion = tk.IntVar()

radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value=1)
radio1.pack()

radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value=2)
radio2.pack()

```
- ### Listbox
```py
lista = tk.Listbox(ventana)
lista.insert(1, "Elemento 1")
lista.insert(2, "Elemento 2")
lista.pack()
```

- ### Scale
```py
escala = tk.Scale(ventana, from_=0, to=100)
escala.pack()
```

- ### Scrollbar
```py
scrollbar = tk.Scrollbar(ventana)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(ventana, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(tk.END, "Elemento " + str(i))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)
```

- ### Canvas
```py
canvas = tk.Canvas(ventana, width=200, height=200)
canvas.pack()

# Dibuja un rectángulo
canvas.create_rectangle(50, 50, 150, 150, fill="blue")
```
- ### Menu
```py
def hacer_algo():
    print("¡Opción seleccionada!")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

submenu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=submenu)
submenu.add_command(label="Abrir", command=hacer_algo)
submenu.add_command(label="Guardar", command=hacer_algo)
submenu.add_separator()
submenu.add_command(label="Salir", command=ventana.quit)
```

- ### MessageBox
```py
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Hola, esto es un cuadro de mensaje!")

boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack()
```
- ### ComboBox
```py
from tkinter import ttk

combobox = ttk.Combobox(ventana, values=["Opción 1", "Opción 2", "Opción 3"])
combobox.pack()
```
- ### ProgressBar
```py
from tkinter import ttk

progress = ttk.Progressbar(ventana, length=200, mode='determinate')
progress.pack()
progress.start()  # Inicia la barra de progreso
```


## Personalización

### Propiedades comunes 

- bg (background): Color de fondo del widget.
- fg (foreground): Color del texto o primer plano.
- font: Fuente y tamaño del texto.
- width y height: Anchura y altura del widget.
- padx y pady: Espacio extra alrededor del widget en los ejes horizontal y vertical.
- relief: Tipo de borde. Los valores pueden ser SUNKEN, RAISED, GROOVE, RIDGE, FLAT.
- state: Define si el widget está habilitado (NORMAL) o deshabilitado (DISABLED).
- cursor: Cambia el tipo de cursor cuando se sitúa sobre el widget.

```py
label = tk.Label(ventana, text="Hola Mundo", bg="yellow", fg="blue", font=("Arial", 16), width=20, height=2)
label.pack(padx=10, pady=5)
```
### Bordes

- FLAT: Sin borde.
- RAISED: Borde elevado.
- SUNKEN: Borde hundido.
- GROOVE: Borde tipo ranura.
- RIDGE: Borde tipo cresta.

```py
frame = tk.Frame(ventana, relief=tk.RIDGE, borderwidth=5)
frame.pack(padx=10, pady=10)
```
### Estados

- NORMAL: Activo y funcional.
- DISABLED: Deshabilitado (el usuario no puede interactuar).
- ACTIVE: Estado visual cuando se interactúa con el widget.

```py
boton = tk.Button(ventana, text="No Funcional", state=tk.DISABLED)
boton.pack()
```

### Iconos y ventanas
- Título de la ventana
Puedes cambiar el título de la ventana usando el método title().
```py
ventana.title("Mi Aplicación Tkinter")
```
- Cambiar el ícono de la ventana
```py
ventana.iconbitmap("ruta_del_icono.ico")
```
- Tamaño y Posición de la Ventana
```py
ventana.geometry("500x300+200+100")
```
esto establece el tamaño de la ventana en 500x300 píxeles y la posiciona a 200 píxeles desde la izquierda y 100 píxeles desde la parte superior de la pantalla.

### Cursor Personalizado
Puedes cambiar el estilo del cursor cuando se pasa sobre un widget con el argumento cursor. Algunos valores comunes son: arrow, circle, cross, hand2, xterm, entre otros.

### Agregar Bordes y Margen con Frame

```py
frame = tk.Frame(ventana, bg="lightgray", relief=tk.GROOVE, borderwidth=5, padx=10, pady=10)
frame.pack(padx=20, pady=20)
```
### Eventos de Hover y Click
Para agregar más interactividad a los widgets, puedes usar eventos como "<Enter>" y "<Leave>" para detectar cuando el mouse pasa por encima de un widget, o "<Button-1>" para clicks del ratón.

```py
def cambiar_color(event):
    label.config(bg="yellow")

def restaurar_color(event):
    label.config(bg="white")

label = tk.Label(ventana, text="Pasa el mouse aquí", bg="white")
label.pack()

label.bind("<Enter>", cambiar_color)
label.bind("<Leave>", restaurar_color)
```
## Posicionamiento 

- pack(): Organiza los widgets en bloques.
- grid(): Organiza los widgets en una cuadrícula.
- place(): Coloca los widgets en posiciones absolutas.

# Ejercicios 

### Ejercicio 1: Personalizar un Label

Crea una ventana que muestre un Label con el texto "Bienvenido a Tkinter". Personaliza el Label con las siguientes especificaciones:

Color de fondo azul.
Texto en blanco.
Fuente Arial tamaño 20, negrita.
El texto debe estar centrado.
Requisitos adicionales:
Añade un margen externo de 20 píxeles alrededor del Label.
**Pista: Usa bg, fg, font, padx, pady.**

### Ejercicio 2: Botón con interacciones
Crea una ventana con un botón que diga "Presiona aquí". Cuando el botón sea presionado, el texto del botón debe cambiar a "¡Has presionado el botón!" y el color de fondo debe cambiar a rojo.

Requisitos adicionales:
Usa una función que cambie el texto y el color cuando se presione el botón.
**Pista: Usa el método config() para cambiar las propiedades del botón cuando se haga clic en él.**

### Ejercicio 3: Formulario simple
Crea un formulario básico con los siguientes elementos:

Un Label que diga "Nombre".
Un Entry donde el usuario pueda escribir su nombre.
Un Button que diga "Enviar".
Al presionar el botón, debe aparecer un nuevo Label en la ventana que diga "Hola, [Nombre]!" donde [Nombre] es el texto que el usuario escribió.

Requisitos adicionales:
Personaliza los Label para que tengan fondo gris claro y texto en negrita.
Usa StringVar para capturar el texto del Entry.

### Ejercicio 4: Manejo de eventos: Hover
Crea una ventana con dos Button que digan "Botón 1" y "Botón 2". Cuando el mouse pase por encima de Botón 1, su color de fondo debe cambiar a verde, y cuando el mouse salga, debe regresar a su color original. Para Botón 2, cambia el color a amarillo cuando el mouse pase por encima.

Requisitos adicionales:
Usa eventos como "Enter" y "Leave" para manejar las interacciones de hover.

### Ejercicio 5: Selector de Color
Crea una ventana que tenga un Label y tres botones que cambien el color del fondo del Label al ser presionados. Los botones deben cambiar el fondo del Label a rojo, verde o azul.

Requisitos adicionales:
El Label debe tener texto que diga "Elige un color".
Usa diferentes funciones para manejar los eventos de cada botón y cambiar el color.

### Ejercicio 6: Deshabilitar Widgets
Crea una ventana con:

Un Checkbutton que diga "Habilitar botón".
Un Button que diga "Enviar", que debe estar deshabilitado al inicio.
Al marcar el Checkbutton, el botón debe habilitarse, y al desmarcarlo, debe deshabilitarse.

Requisitos adicionales:
Usa la propiedad state con los valores NORMAL y DISABLED para habilitar y deshabilitar el botón.

### Ejercicio 7: Interfaz de Login Simple
Crea una interfaz de login con los siguientes elementos:

Un Label que diga "Usuario" y otro que diga "Contraseña".
Dos Entry para que el usuario introduzca su nombre y contraseña.
Un Button que diga "Login".
Al presionar el botón, si el campo de usuario está vacío, debe aparecer un mensaje en rojo debajo diciendo "El campo usuario no puede estar vacío". Si no está vacío, debe mostrar un mensaje en verde diciendo "Bienvenido, [usuario]".

Requisitos adicionales:
Cambia el color del mensaje dependiendo de si es un error o un saludo.

### Ejercicio 8: Barra de Progreso
Crea una ventana con:

Un Button que diga "Iniciar Proceso".
Una Progressbar que avance del 0% al 100% en 5 segundos cuando el botón sea presionado.

Requisitos adicionales:
Usa ttk.Progressbar y el método start() para manejar la barra de progreso.

### Ejercicio 9: Calculadora Básica
Crea una pequeña calculadora con los siguientes elementos:

Un Entry para que el usuario ingrese dos números separados por un espacio.
Cuatro Button que representen las operaciones: suma, resta, multiplicación y división.
Un Label donde se muestre el resultado.

Requisitos adicionales:
Cada botón debe ejecutar la operación correspondiente y mostrar el resultado en el Label.