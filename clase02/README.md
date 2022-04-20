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
