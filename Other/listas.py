A = [5, 2, 8, 4, 1, 6, 10, 9]
B = [1, 3, 5, 6, 6, 7, 11, 4]
C = []

for i in range(0, len(A), 1):
    valor = A[i] + B[len(A) - i - 1]
    C.append(valor)

print(C)

import math

r = 2 * math.pi
