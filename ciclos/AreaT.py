n = int(input())
l = float(input())
inc = float(input())
a = 0
for i in range(1, n + 1):
    a += l ** 2
    l += inc
print("El area total es de", a, "metros cuadrados")
