#CLASE 1
print("Hola Mundo")
print('Saludamos desde Python en la primer clase de laboratorio')
# CLASE 2
miVariable = 3  # Declaramos una variable que guarda un valor Integer
print(miVariable)  # Imprimo por consola
miVariable = 'Buenas tardes a todos los alumnos'   # Vemos que es dinamico y puedo asignarle primero un numero (Integer) y luego String
print(miVariable)  # Imprimo por consola
miVariable = 3.5  # Y ahora le asigno otro valor, paso de Integer a Float
print(miVariable)  # Imprimo por consola
x = 10
y = 2
print(f'x={x} sumada a y={y}, da {x+y}')  # para concetenar String con varaibles
print(id(x))  # para ver el espacio en memoria que esta ocupando mi variable, es la referencia en memoria
print(id(y)) # para ver el espacio en memoria que esta ocupando mi variable, es la referencia en memoria
# CLASE 3
frase = "Hola alumnos"  # frase: str = "Hola alumnos"
print(type(frase)) # <class 'str'>
valorBooleano = True
print(type(valorBooleano))  # <class 'bool'>
valorNumero = 10
print(type(valorNumero)) # <class 'int'>
valorNumero = 10.4
print(type(valorNumero)) # <class 'float'>