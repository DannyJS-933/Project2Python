
# wordList = []
#
# for i in range(0, 10):
#     word = (input('Ingrese una palabra: '))
#     wordList.append(word)
# print(f'Lista original: {wordList}')
#
# lastList = set(wordList) #set remueve duplicados en una lista
# print(f'Lista sin duplicados: {lastList}')


#-------------------------------------------------
print('Segunda parte del ejercicio 12')
newList = []

for i in range(0,5):
    creatingList = (input('Ingrese una palabra: '))
    newList.append(creatingList)
print(newList)

duplicates = []
for i in newList:
    if newList.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)








