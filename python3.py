import random
from math import sqrt

def parz(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
n = int(input('n='))
x = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1, 50))
    x.append(row)
print("Matrix x:")
for row in x:
    print(row)
y = []
for i in range(n):
    prime_count = 0  
    for j in range(n):
        if parz(x[i][j]):
            prime_count += 1  
    y.append(prime_count)  
print()
print(y)