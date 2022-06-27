# :book: Ejercicios de practica para las vacaciones

---

Sacados de [http://patriciaemiguel.com/ejercicios/python/2019/02/24/ejercicios-principiantes-python.html](http://patriciaemiguel.com/ejercicios/python/2019/02/24/ejercicios-principiantes-python.html)

---

## :star: Sección 1

### Entrada/salida de datos - Variables - Tipos de datos  

Código de ejemplo
```Python
Variable=5
variable=3
VaRiAbLe=8
```

->Son todas variables distintas porque Python (como muchos otros lenguajes) distingue mayúsculas y minúsculas.
Código de ejemplo

```Python
a=5
a=18
```

-> a tomará el último valor asignado (lo que tuviera guardado anteriormente la variable, se pierde).

```Python
1variable=23.95
```

-> Arroja error porque los nombres de variables sólo pueden comenzar con letras o guiones bajos (_).

```Python
n1=int(input())
n2=float(input())
```

-> Sabemos que input() lee lo que el usuario escribe en el programa, pero el tipo de eso que lee será siempre string. Si necesitamos que sea un número debemos convertir lo que input() devuelve. Para convertir a número entero usamos int(input()) y para convertir a número con decimales usamos float(input()).

---

### EJERCICIO 1

Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.
 
Ejemplo de ejecución:
```
Tu nombre: Patricia
Ahora estás en la matrix, Patricia
```

---

### EJERCICIO 2

Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.
 
Ejemplo de ejecución:
```
Primer número: 14.2
Segundo número: 19
El resultado de la suma es 33.2
```

---

## EJERCICIO 3

Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
 
Ejemplo de ejecución:
```
Ingresá un número: 1
Ingresá otro número: 2
Suman: 3
Ingresá un nuevo número: 3
Multiplicación de la suma por el último número: 9
```

---
