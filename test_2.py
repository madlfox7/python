import random
from numpy import *
from math import *

def parz(a):
    if a <= 1:
        return False
        for j in range(2, int(sqrt(a)) + 1):
            if a % j == 0:
                return False
            else:
                return True

n= int(input("Enter a positive integer:"))
x=random.randint(-10, 35, size = n)
print(x)
y = []
for i in range(len(x)):
    if parz(x[i]) == True:
        y.append(x[i])
print(y)

