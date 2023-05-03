from math import sqrt

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())


def dist(a, b):
    d = sqrt((a ** 2) + (b ** 2))
    return round(d, 2)

ds = []

ds.append(dist(x1, y1))
ds.append(dist(x2, y2))
ds.append(dist(x3, y3))

for i in range(3):
    print("El carro {} esta a {} kilometros".format(i + 1, ds[i]))

print("El carro {} esta mas cercano al incendio".format(ds.index(min(ds)) + 1))
