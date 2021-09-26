#Crear una lista de numeros y sumar los numeros dentro de la lista

import random

randomList = []

randomList = random.sample(range(0, 15), 5)
print(randomList)

sumList = sum(randomList)
print(f'Esta es la suma de los numeros dentro de la lista: {sumList}')