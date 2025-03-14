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
S = 0
y = []
for i in range(n):
    row_sum = 0  
    for j in range(n):
        if parz(x[i][j]):
           # print(f'Prime found: {x[i][j]} at position ({i}, {j})')
            row_sum += x[i][j]
    y.append(row_sum)  
print("Sum of primes in each row:", y)