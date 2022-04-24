# Clase 1: Fundamentos Python 

## Temas:

- 1.1 Instalación de Python 3

- 1.2 Instalación de Pycharm

- 1.3 Características generales de Python. Ver TIOBE (estadística de los lenguajes de programación)

- 1.4 Hola Mundo con Python

- 1.5 Actividad: Saludar con Python

---

## :star: 1.1 Instalación de Python 3

- Desde [python.org/downloads](python.org/downloads) para bajar e instalar **Python**

- Recordar tildar las dos opciones: Add Python 3.10 to PATH / Install launcher for all users

- Hacer click en customizar la instalación

- Tildar todas las 6 opciones -> Next

- En las opciones avanzadas tener seleccionadas las primeras 5 y abajo esta la ruta de instalación por default -> Install


---

## :star: 1.2 Instalación de Pycharm

- Vamos a [https://www.jetbrains.com/pycharm/download/#section=windows](https://www.jetbrains.com/pycharm/download/#section=windows), buscamos la opción Commmunity

- Click en *Descargar* en la opción *Community*

- Se abre la ventana de instalación, se ve la ruta de instalación -> Next -> Next -> Install

Una vez instalado en **customize** se le puede elegir el fondo del Ide, el tamaño de la letra, etc.

Desde **Proyects** se puede iniciar el proyecto.

---

## :star: 1.3 Características generales de Python. Ver TIOBE (estadística de los lenguajes de programación)

Python es un lenguaje de programación creado por Guido van Rossum en el Centro para las Matemáticas y la Informática (CWI - Holanda) en 1991.

Suscaracterísticas:


- Es un lenguaje de programación **multiparadigma**

- Es **multiplataforma** (Windows, Linux, Mac)

- Es muy **sencillo de aprender** ya que es un lenguaje simple y minimalista

- Es **interpretado**, se va ejecutando linea por linea.

- Usa **tipado dinámico**, una variable puede almacenar distintos tipos de datos a lo largo del programa (por ejemplo una varaible que alamcene un numero luego puede alamcenar un caracter).


## ¿ Qué se puede programar con Python ?

Python es un lenguaje de proposito general, casi todo puede programarse con Python.

Python es un lenguaje de **proposito general**, casi todo puede programarse con él:

- aplicaciones web

- juegos

- aplicaciones a medida

- inteligencia artificial


## Entorno de Desarrollo (IDE)

Hay muchos, algunos:

- Visual Studio Code

- PyCharm

- PyDev

- Sublime Text3

- ATOM

- VIM

---

## :star: 1.4 Hola Mundo con Python

Se puede usar comillas dobles:

```Print("Hola Mundo")```

Se puede usar comillas simples:

```Print('Hola mundo')```

Lo importante es no mezclarlas, si se inicia con comillas dobles se cierra con comillas dobles.

---

## :star: 1.5 Actividad: Saludar con Python

En el archivo [clase01.py](https://github.com/eugenia1984/UTN-FRSR-Laboratorio-de-computacion-1/blob/main/clase01_02_03/main.py) está la mini practica




---
---


# Clase 2: Variables en Python

## Temas:

- 2.1 Variables Parte 1

- 2.2 Dirección de memoria y variables

---

## :star: 2.1 Variables

- Básicamente una variable nos va a permitir guardar información de manera temporal.

- Esta información puede se un valor numérico, tipo cadena una fecha, etc.

- Vamos a poder usarla tantas veces como lo necesitemos, antes de que termine nuestro programa o que sea destruida esta variable.

- Ahora vemos como declarar y utilizar una variable en Python:

```Python
myName= "Bob"
myAge = 17
isHAppy = True
```

Tenemos: ` identificador = dato/valor`

El **=** es el operador de asignación

- Para la ejecucion siempre se debe tener en cuenta los atajos del teclado:

`Ctrl + Mayús + F10 -> Run `

- Una ventaja al utilizar variables es que en un solo lugar podemos hacer un cambio del valor que almacena, el cambio se verá reflejado en todos los lugares donde estemos utilizando esta variable.

- Una ventaja en Python, es que no tenemos que indicar el tipo de la variable, por esto podemos cambiar el valor.

Una literal es un valor que podemos asignar a nuestras variables -> A esto se lo conoce como referencia de memoria o simplemente Referencia

Practica

```Python
miVariable = 3  # Declaramos una variable que guarda un valor Integer
print(miVariable)  # Imprimo por consola
miVariable = 'Buenas tardes a todos los alumnos'   # Vemos que es dinamico y puedo asignarle primero un numero (Integer) y luego String
print(miVariable)  # Imprimo por consola
miVariable = 3.5  # Y ahora le asigno otro valor, paso de Integer a Float
print(miVariable)  # Imprimo por consola
```

- Básicamente una **función** nos permite ejecutar cierto código: en el caso print nos permite imprimir el valor de una variable hacia la consola (Esto lo veremos en funciones)

- La función que nos permite ejecutar el código para imprimir los datos:

```Python
print()
```

---

## :star: 2.2 Dirección de memoria y variables

- ¿ Que sucede en la memoria Ram?

En nuestro espacio de memoria Ram hay casillas, cada una va a almacenar la información de nuestros programas (seria la información que estamos asignando a las variables)

Cada variable va a apuntar a un espacio en memoria(cada una a una única opción).

- Cada valor es una **literal**: una literal es un valor que podemos asignar a nuestras variables, la literal 10 que es un valor numérico, lo asignamos a nuestra variable x, la literal 2 se asigna a y, las dos están en diferentes posiciones de memoria

- Para saber la dirección de memoria donde están estas literales hacemos esto: Tenemos la dirección **id**, y utilizamos la función:

```Python
id(x)
print(id(x))    # una función dentro de otra
```

- En numero que vemos en consola, solo tomemos los 3 últimos por ejemplo: x278

- Ya que normalmente las direcciones de memoria son valores hexadecimales y los valores hexadecimales se les antepone una x, en este caso la x que ponemos no tiene nada que ver con la variable, la enseñanza es que una variable apunta a cierta dirección de memoria.

- Sin embargo, si volvemos a ejecutar el código no vamos a obtener la misma posición de memoria, ya que estas variables al almacenar en la memoria Ram, están constantemente moviéndose en diferentes direcciones de memoria en cada ejecución.

- Por esto nunca vamos a obtener los mismos valores.

- Ahora observamos tres casillas donde se almacenan las literales.

**A ESTO SE LO CONOCE COMO REFERENCIA DE MEMORIA O SIMPLEMENTE REFERENCIA**.

```
x   ->   x626   Guarda 10
y   ->   x478   Guarda 2
z   ->   x849   Guarda 12
```

- Así es que cada una de estas casillas contiene una dirección de memoria que se le ha asignado y dentro tenemos el valor de la literal almacenado.

- En la practica: Ejecutamos nuevamente y las direcciones van a cambiar.

- ¿Por qué pasa esto? Es porque cuando ejecutamos el programa: arranca, reserva memoria, termina y volvemos a ejecutar (recordemos que la memoria es volátil) esto quiere decir que el terminar de ejecutar nuestro programa se eliminan todas la variables y se vuelven a crear cada vez que ejecutamos.

**ESTO ES IMPORTANTE PARA ENTENDER NUESTRAS VARIABLES EN PYTHON!!!**

---
---


# Clase 3:   Tipos de datos en Python

## Temas:

- 3.1 Tipos de datos

- 3.2 Manejo de cadenas

- 3.3 Más temas de manejo de cadenas

- 3.4 Tipos Boleanos (Bool)

- 3.5 Procesar entrada del usuario (Función input)

- 3.6 Conversión de la entrada de datos

- 3.7 Actividad: Ejercicio Califica tu día

---

## :star:  3.1 Tipos de datos

- numericos: Integer, Complex, Float

- Boolean (booleano)

- Set

- : String, List (lista), Tuple (tupla)

- Dictionary (diccionario)


Ejemplo de String

```Python
frase = "Hola alumnos"  # frase: str = "Hola alumnos"
print(type(frase)) # <class 'str'>
```

Ejemplo de Boolean:
```Python
valorBooleano = True
print(type(valorBooleano))  # <class 'bool'>
```

Ejemplo de numero entero:
```Python
valorNumero = 10
print(type(valorNumero)) # <class 'int'>
```

Ejemplo de numero float (flotente/decimal):
```Python
valorNumero = 10.4
print(type(valorNumero)) # <class 'float'>
```



---

## :star: 3.2 Manejo de cadenas

Si tengo dos String y le aplico **+** entonces concateno.

```Python
numero1 = "7"
numero2 = "8"
print(numero1+numero2) # 78
```

---


## :star:  3.3 Más temas de manejo de cadenas


Casteo de String a numero

```Python
numero1 = "7"
numero2 = "8"
print(int(numero1)+int(numero2)) # 15
```

---


## :star: 3.4 Tipos Boleanos (Bool)

Permite saber si es Verdadero o Falso.

Ejemplo en codigo:

```Python
miBooleano = 3>2
print(miBooleano)

if miBooleano:
  print("El resultado es verdadero")
else:
  print("El resultado es falso")
```

---


## :star: 3.5 Procesar entrada del usuario (Función input)


Se utiliza el método **input**, como input nos regresa un dato de tipo cadena, lo puedo castear a int o float si es que necesito un numero en vez de un String, ejemplo en codigo:

```Python
numeroIngresado1 = int(input("Ingrese un numero: "))
numeroIngresado2 = int(input("Ingrese otro numero: "))
resultado = numeroIngresado1 + numeroIngresado2
print(f"El primer numero ingresado es: {numeroIngresado1}") 
print(f"El segundo numero ingresado es: {numeroIngresado2}") 
print(f"La suma de ambos es: {numeroIngresado1 + numeroIngresado2}") 
```

---


## :star: 3.6 Conversión de la entrada de datos

Todo lo que se ingresa con **input** ingresa de como tipo **Stting** para castearlo a numero, en caso de necesitr hacer cuentas se utiliza **int**

Y para castear del otro modo, de String a Number se utiliza **str**

Un ejemplo de casteo de String a int:
```Python
numeroIngresado1 = int(input("Ingrese un numero: ")) 
```
---


## :star: 3.7 Actividades de practica: 

### Ejercicio 1: Califica tu día : 

Por pantalla debe aparecer: **¿Cómo estuvo tu día (1 al 10)?**

El usuario ingresa el dia, y por pantalla sale:

**Mi día estuvo de: 10** , en el caso de que el usuario ingreso 10

### Ejercicio 2:

Se solicita incluir la siguiente información acerca de un libro:

**titulo**

**autor**

Debes imprimir la información en el siguiente formato:

**Proporciona el título:**

**Proporciona el autor:**

Y que por pantalla se vea: ```<titulo> fue escrito por <autor>```


---
---
