# calcular la suma de "N" primeros numeros
cantidad_de_numeros_a_sumar = int(input('Ingrese la cantidad de números a sumarse: '))
suma_total = 0 # para guardar la sumatoria de numeros
contador = 0 # para ir contando las iteraciones del loop
for contador in range (1, cantidad_de_numeros_a_sumar + 1):
  suma_total = suma_total + contador
  contador += 1
print(f'La suma total es {suma_total}')
