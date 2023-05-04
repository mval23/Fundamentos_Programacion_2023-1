n = int(input())
fila = []
orden = []

for i in range(n):
    fila.append(float(input()))

orden = fila.copy()
orden.sort()

for i in orden:
    print(fila.index(i) + 1)