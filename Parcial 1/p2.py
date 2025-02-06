from random import random
import matplotlib.pyplot as plt

#Funcion para simular el dado con transformada inversa
def dado():
  r = random()
  if r < 1/6:
    return 1
  elif r < 2/6:
    return 2
  elif r < 3/6:
    return 3
  elif r < 4/6:
    return 4
  elif r < 5/6:
    return 5
  else:
    return 6

#Funcion para simular la situacion de tirar el dado y avanzar en el juego de mesa
def simulacion(n):
  lista = []

  for i in range(n):
    pos = 0
    while pos < 100:
      pos += dado()
      if pos <= 100: lista.append(pos)
  
  return lista

#Graficar los datos obtenidos
datos = simulacion(10000)

# Crear el histograma
plt.hist(datos, bins=len(set(datos)), edgecolor='black')

# Añadir etiquetas y título
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el histograma
plt.show()

# Los numeros donde deberia poner las monedas son
frecuencias = {}
for i in datos:
  if i not in frecuencias:
    frecuencias[i] = 1
  else:
    frecuencias[i] += 1

frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)

print(f"La posicion 1 es {frecuencias_ordenadas[0][0]} con una cantidad de observaciones de {frecuencias_ordenadas[0][1]}")
print(f"La posicion 2 es {frecuencias_ordenadas[1][0]} con una cantidad de observaciones de {frecuencias_ordenadas[1][1]}")
print(f"La posicion 3 es {frecuencias_ordenadas[2][0]} con una cantidad de observaciones de {frecuencias_ordenadas[2][1]}")