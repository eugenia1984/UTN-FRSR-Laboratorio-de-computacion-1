# Valor dentro de un rango
# 1- Pedimos al usuario un valor numerico
# 2- Verificar si el valor ingresado se encuentra entre el rango 0 a 5, 0 y 5 inclusive
numeroIngresado = int(input("Ingresa un numero: "))
if numeroIngresado>=0 and numeroIngresado<=5:
  print("El numero ingresado esta en el rango 0-5")
else:
  print("El numero ingresado no esta en el rango de 0-5")