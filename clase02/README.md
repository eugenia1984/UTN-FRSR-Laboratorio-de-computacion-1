# Clase 2:  Variables en Python

## Temas:

- 2.1 Variables Parte 1

- 2.2 Dirección de memoria y variables

---

## :star: 2.1 Variables 

- Básicamente una variable nos va a permitir guardar información de manera temporal.

- Esta información puede se un valor numérico, tipo cadena una fecha, etc.


- Vamos a poder usarla tantas veces como lo necesitemos, antes de que termine nuestro programa o que sea destruida esta variable.

- Ahora vemos como declarary utilizar una variable en Python:

```Python
myName= "Bob"
myAge = 17
isHAppy = True
```

Tenemos: ``` identificador = dato/valor```

El **=** es el operador de asignación

- Para la ejecucion siempre se debe tener en cuenta los atajos del teclado:

```Ctrl + Mayús + F10 -> Run  ```

- Una ventaja al utilizar variables es que en un solo lugar podemos hacer un cambio del valor que almacena, el cambio se verá reflejado en todos los lugares donde estemos utilizando esta variable.

- Una ventaja en Python, es que no tenemos que indicar el tipo de la variable, por esto podemos cambiar el valor.

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


---
