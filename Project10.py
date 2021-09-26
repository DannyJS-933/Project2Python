#Crear una lista de numeros, imprimir la lista original y una nueva en el orden invertido

import random

randomList = []

randomList = random.sample(range(0, 20), 20)
print(f'Lista original: {randomList}')

randomList.reverse()
print(f'Lista inversa: {randomList}')