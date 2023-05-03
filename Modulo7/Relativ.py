from math import sqrt

n = int(input())
l = []


def lorentz(v):
    c = 299792458
    v *= (10 / 36)
    a = 1 - ((v ** 2) / (c ** 2))
    y = round((1 / (sqrt(a))), 15)
    return round(y, 15)


for i in range(n):
    l.append(lorentz(float(input())))

for j in l:
    print(j)
