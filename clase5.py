# Valor dentro de un rango
# 1- Pedimos al usuario un valor numerico
# 2- Verificar si el valor ingresado se encuentra entre el rango 0 a 5, 0 y 5 inclusive
numeroIngresado = int(input("Ingresa un numero: "))
if numeroIngresado>=0 and numeroIngresado<=5:
  print("El numero ingresado esta en el rango 0-5")
else:
  print("El numero ingresado no esta en el rango de 0-5")

# Operador logico OR
vacaciones = False
diaDescanso = False

if vacaciones or diaDescanso:
  print("Puede asistir al juego")
else:
  print("Tiene trabajo que hacer")

# Rango entre las edades 20 y 30 años
# 1- Preguntar la edad al usuario
# 2- Si la edad esta dentro de los 20 o 30 años está dentro del rango
# 3- Combinamos los operadores and y or para saber si el usuario esta dentro del rango o no
edadIngresada = int(input("Ingrese su edad : "))
veinte = edadIngresada>=20 and edadIngresada<30
treinta = edadIngresada>=30 and edadIngresada<40
if veinte or treinta:
  print("Esta dentro del rango de los 20`s a 30's años")
else:
  print("No esta dentro del rango")