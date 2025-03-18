from math import *
from numpy import *


def parz(a):
    if a <= 1:
        return False
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                return False
            return True

n = int(input('Enter positive integer:'))
x = random.randint(-10, 35, size=(n, n))
print(x)
y = []
for i in range(n):
    for j in range(n):
        if parz(x[i][j]):
            y.append(x[i][j])
print(y)
z = random.randint(10, 35, size=n)
print(z)
for i in range(n):
    for j in range(n):
        if z[i] > z[j]:
            z[i], z[j] = z[j], z[i]
print(z)


#review later