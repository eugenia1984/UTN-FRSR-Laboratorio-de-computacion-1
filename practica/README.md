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


### EJERCICIO 4

Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.
 
Ejemplo de ejecución:
```
Kilómetros recorridos: 260
Litros de combustible gastados: 12.5
El consumo por kilómetro es de 20.8
```

---

### EJERCICIO 5

Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
 
Ejemplo de ejecución:

Ingresá una temperatura expresada en Farenheit: 75
23.88888888888889

6
Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
 
Ejemplo de ejecución:

Primer número: 8.5
Segundo número: 10
Tercer número: 5.5
El promedio de los tres es 8.0

7
Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.
 
Ejemplo de ejecución:
```
Ingresá un número: 260
Descontando el 15% queda: 221.0
```

Código de ejemplo

```Python
cadena=""
cadena=cadena+"buen"
cadena=cadena+" día"
print(cadena)
```

-> Cuando se utiliza el operador + en una operación entre strings, se está realizando una concatenación (unión de strings). La instrucción print mostrada arriba imprimirá “buen día”.

---

## EJERCICIO 8

Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.
 
Ejemplo de ejecución:
```
Primera palabra: derribando
Segunda palabra: muros
derribando muros
```

Código de ejemplo

```Python
frase="Estoy programando"
print(frase[0])
i=6
print(frase[i])
```

-> El operador [ ] (corchetes) permite obtener un carácter a partir de un string. La posición del carácter se indica entre los corchetes, ya sea ingresando directamente el número, con una variable que contenga un número o con una operación que de como resultado un número. Siempre, el primer carácter de un string estará ubicado en la posición 0.

Código de ejemplo

```Python
frase="Estoy programando"
print(len(frase))
ultimo_caracter=frase[len(frase)-1]
print(ultimo_caracter)
```

-> Mediante len() podemos obtener la cantidad de caracteres que contiene un string. Este valor siempre será un número entero (tipo int) y puede guardarse en una variable, imprimirse, usarse en una operación aritmética, etc.

---


## EJERCICIO 9

Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.

Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
 
Ejemplo de ejecución:

```
Ingresá un texto: En un lugar de La Mancha, de cuyo nombre no quiero acordarme…
El carácter en primer lugar es: E
Ingresá un número positivo menor a 63
7
El carácter en esa posición es: u
```

Código de ejemplo

```Python
a=10
b=4
print(a != b)
```

-> La instrucción print imprimirá True, ya que el valor contenido en a es diferente del valor contenido en b.

---

## EJERCICIO 10

Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.
 
Ejemplo de ejecución:
```
Shows vistos en el último año: 3
False
```

Código de ejemplo

```Python
print(58273%10)
print(58273//10)
```

-> La primera instrucción imprimirá el número 3, ya que es el resto de la división de 58273 por 10. La segunda instrucción imprimirá 5827, ya que es la parte entera del resultado de dividir 58273 por 10. Estas operaciones matemáticas son estrategias que se pueden utilizar para obtener partes de un número.

---

## EJERCICIO 11

Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
 
Ejemplo de ejecución:
```
Fecha en formato DDMMAAAA: 16112017
16 / 11 / 2017
```

---


## EJERCICIO 12

Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.
 
Ejemplo de ejecución:
```
Número entero: 7254
True
```

Código de ejemplo
```Python
a=int(input())
print(a>100  and  a!=1000)
```

-> Primero se calcularán los valores lógicos (True o False) de las dos comparaciones: a > 100 y a != 1000 (lo cual dependerá del número guardado en la variable a). A continuación, se utilizará la tabla de verdad de la operación AND para calcular el resultado.

---

## EJERCICIOS 13

Escribí un programa que le solicite al usuario su edad y la guarde en una variable. Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo.
 
Ejemplo de ejecución:
```
Tu edad: 32
Artículos comprados: 1
False
```

---

## EJERCICIO 14

Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.
 
Ejemplo de ejecución:
```
Ingresá una frase: Era el mejor de los tiempos, era el peor de los tiempos.
True
```


Código de ejemplo
```Python
"animal" > "piedra"
"bailar” > "bebida"
```

-> Ambas comparaciones arrojan True porque el string “animal” es menor que “piedra” y el string “bailar” es menor que “bebida”. El orden está dado por cómo aparecen las letras en el alfabeto. En el caso de “animal” y “piedra”, la “a” es menor que la “p”. En el caso de “bailar” y “bebida”, como la primera letra es la misma se evalúa la segunda, y en este caso “a” es menor que “e”.

---

## EJERCICIO 15

Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.
 
Ejemplo de ejecución:
```
Una palabra: complejidad
Otra palabra: algoritmo
False
```

---

## EJERCICIO 16

Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona, almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True, ya que ambos comienzan con la misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True, ya que ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se mostrará False, ya que no coinciden ni la primera ni la última letra.
 
Ejemplo de ejecución:
```
Tu nombre: Alfredo
Otro nombre: Eduardo
True
```


---
---
