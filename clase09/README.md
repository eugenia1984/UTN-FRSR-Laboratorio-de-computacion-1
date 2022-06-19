## :book: Clase 9 - 15 de Junio

---

### Ejercicios de practica

**Ejercicio 1**: Diseñar un programa que ingresando un año, nos devuelva por sonsola si es un año bisiesto o no, repetir la accion hasta que el usuario lo desea.

Y... ¿ cuando un año es bisiesto?

- Un año es bisiesto si es: Divisible entre 4. No divisible entre 100. Divisible entre 400.

- Una manera sencilla y compacta de saber si un año es bisiesto en Python, y suponiendo que la variable a contiene el año a comprobar, es utilizar la siguiente condición: not a % 4 and (a % 100 or not a % 400). Otra manera es usar la función isleap del módulo calendar.

Matemáticamente podemos saber si un año es bisiesto si este es múltiplo de 4. Si además es múltiplo de 100 no será bisiesto (ten en cuenta que 100 es múltiplo de 4 y por tanto cualquier número que sea múltiplo de 100 también es múltiplo de 4) a no ser que sea múltiplo de 400, que sí será bisiesto.

| ¿Múltiplo de 4? |	¿Múltiplo de 100?	| ¿Múltiplo de 400?	| Es bisiesto |	Ejemplos |
| --------------- | ----------------- | ----------------- | ----------- | -------- |
| No	| No	| No	| No	| 2019, 1981 |
| Sí	| No	| No	| Sí	| 2020, 2012 |
| Sí	| Sí	| No	| No	| 1900, 2100 |
| Sí	| Sí	| Sí	| Sí	| 2000, 2400 |

Tenemos que tener en cuenta que para calcular si un número es múltiplo de otro podemos usar el operador módulo o resto, que calcula el resto de la división entera entre dos números. Si el resto es 0 quiere decir que el divisor divide al dividendo y que por tanto el dividendo es múltiplo del divisor. También se dice que si un número a es múltiplo de un número b, b divide a. O que b es divisor de a. En Python el operador de módulo es %.

También es importante conocer los operadores booleanos and y or que nos permiten combinar varias condiciones sencillas en una sola compleja, así como el operador de comparación != que nos indica si dos valores son diferentes.

```Python
anio = 0
anio = int(input(f'Ingrese un año para informarle si es bisiesto \nCuando quiera salir ingrese doble cero "00"... ')) # el año que queremos comprobar
while anio != 00:
  # Usando un operador ternario
  print("Es bisiesto" if not anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)  else 'No es bisiesto')
  anio = int(input(f'Ingrese un año para informarle si es bisiesto \nCuando quiera salir ingrese doble cero "00"... ')) # el año que queremos comprobar
```

->> se puede ver el codigo en **anio_bisiesto.py**

---

**Ejercicio 2**: calcular la suma de "N" primeros numeros

```Python
# calcular la suma de "N" primeros numeros
cantidad_de_numeros_a_sumar = int(input('Ingrese la cantidad de números a sumarse: '))
suma_total = 0 # para guardar la sumatoria de numeros
contador = 0 # para ir contando las iteraciones del loop
for contador in range (1, cantidad_de_numeros_a_sumar + 1):
  suma_total = suma_total + contador
  contador += 1
print(f'La suma total es {suma_total}')
```

->> se puede ver el codigo en **suma_de_n_numeros.py**

---