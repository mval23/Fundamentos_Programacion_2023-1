n = int(input())
l = list(range(1, n + 1))
l1 = []
for i in range(n - 1):
    l1.append(int(input()))

for j in l:
    if j not in l1:
        print("La ficha faltante es la {}".format(j))
