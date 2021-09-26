#Replace negative values to positive.

myFirstList = {-2, -1, 15, 1, 2, 3};
myFirstList.add(-4)

changeValue = [ (i > 0) * i for i in myFirstList]
print(changeValue)

