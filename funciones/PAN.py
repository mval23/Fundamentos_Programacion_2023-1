from math import sqrt
def P(x):
    return 2*x + 1
def A(x):
    return 3**x
def N(x):
    return sqrt(5*x + 4)


m = int(input())
l = []
for i in range(m):
    l.append(P(A(N(float(input())))))

for j in l:
    print(j)