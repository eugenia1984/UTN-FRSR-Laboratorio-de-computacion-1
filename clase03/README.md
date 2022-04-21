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

---


## :star: 3.7 Actividad: Ejercicio Califica tu día

---
