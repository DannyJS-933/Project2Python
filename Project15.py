import random

randomList = []

randomList = random.sample(range(0,10), 8)
print(randomList)

for i in randomList:
    double = i ** 2
    print (double)