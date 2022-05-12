# :book: Clase 6 : 11 Mayo - Condicionales




## :star: IF -  ELSE

Generalmente la sentencia **if - else** nos lleva a seleccionar un camino u otro.

Podemos observar el algoritmo, en la condición debemos saber que lleva una expresión booleana, donde tenemos el valor de Verdadero, Falso, solo se ejecuta uno de los dos.

```
      |
      v
CONDICION IF - ELSE
 |               |
 V               V
Instruccion   Instruccion
 |               |
 v ------------- v
```

-> Un dato importante: La identación solo necesita un espacio, sabemos que el tabulador tiene cuatro espacios, pero para la identación solo uno es suficiente para quitar el error, ahora lo más común es hacer uso del tabulador y si hay otras sentencias anidadas pues deberemos utilizar más tabuladores.


-> La única sentencia obligatoria es la if, no así el elif y el else, ya que estas quedan al uso y criterio del programador, según el uso que le quiera dar al algoritmo


```Python
condicion = false

if condicion:
  print("Condicion verdadera")
else:
  print("Condicion falsa")
```  

Lo podes ver en codigo en **clase6.py**

## :star: IF - ELIF - ELSE

```Python
condicion = 1

if condicion == True:
  print("Condicion verdadera")
elif condicion == False:
  print("Condicion falsa")
else:
  print("Condicion sin especificar")
```

Si condicion = True -> imprimie Condicion verdadera

Si condicion = False -> se imprime Condicion falsa

Si condicion = 0 -> se imprime Condicion falsa --> **0 es igual a False**

Si condicion = 1 -> se imprimi Condicion verdadera --> **1 es igual a  True**

Si condicion = '' -> se imprime Condicion sn especificar

Si condicion = 20 -> se imprime Condicion sn especificar

Lo podes ver en codigo en **clase6.py**

---

## Segundo ejercicio para practicar IF - ELIF - ELSE

```Python
num = int(input("Ingrese un numero en el rango de a al 3: "))
numTexto = ''

if num == 1:
  numTexto = 'Numero uno'
elif num == 2:
  numTexto = 'Numero dos'
elif num == 3:
  numTexto = 'Numero 3'
else:
  numTexto = 'Has ingresado un número fuera de rango'

print(f'El número ingresado es: {num} - {numTexto}')
```

Lo podes ver en codigo en **clase6.py**

---

## Tercer ejercicio

Escribir la siguiente expresion en forma de expresion algoritmica

```
A3 x (b2 - 2ac)
-
2b
```

Pedimos al usuario que ingrese los valores de a, b, c y mostramos el resultado


```Python
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
resultado = ( a **3 * (b ** 2 - 2 * a * c) / (2*b))
print(f'El resultado es {resultado}')
```

Lo podes ver en codigo en **expresion.py**

---

## :star: Operador ternario

```Python
condicion = True
print('Condicion Verdadera') if condicion else print('condicion Falsa')
```

Lo podes ver en codigo en **ternario.py**
---

## Cuarto ejercicio

Determinar la solución lógica de la siguiente operación.

((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b)

```Python
a = int(input("Ingresa un numero entero: "))
b = int(input("Ingresa otro numero entero: "))
print(f'La expresion: ((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b) da como resultado: {((3 + 5 * 8 ) < 3 and ((- 6/3 * 4 ) + 2 < 2)) or ( a > b)}')
```

Podes ver el codigo en **expresion_logica.py**

---

## Quinto ejercicio

Intercambiar el valor de dos variables.

Por ejemplo: 

a = 10   ->  a = 5

b = 5   ->   b = 10

```Python
numeroIngresado1 = int(input("Ingresa un valor: "))
numeroIngresado2 = int(input("Ingresa un segundo valor: "))
valorAuxiliar = numeroIngresado1
numeroIngresado1 = numeroIngresado2
numeroIngresado2 = valorAuxiliar
print(f"Intercambiando los valores de los numeros ingresados\nEl primero es {numeroIngresado1}\nY el segundo es {numeroIngresado2}")
```

Podes ver el codigo en **intercambiar_valor.py**

---

## : Sexto ejercicio: Área y longitud de un circulo

Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.

Área = Pi * r2

Longitud = 2 * Pi * r

En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi

Se escribe:   import math

Podes ver el codigo en **circulo.py**

---
---