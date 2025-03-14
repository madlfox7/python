import random
from math import sqrt

def pow_of(num):
    if num < 1:
        return False
    while num % 3 == 0:
        num //= 3
    return num == 1

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
found = False
for i in range(n):
    for j in range(n):
        if pow_of(x[i][j]):
            row_to_del = i
            col_to_del = j
            found = True
            break
    if found:
        break

if found:
    x.pop(row_to_del)
    for row in x:
        row.pop(col_to_del)
    print("\nMatrix after deleting row", row_to_del, "and column", col_to_del, ":")
    for row in x:
        print(row)
else:
    print("No element satisfies the condition.")