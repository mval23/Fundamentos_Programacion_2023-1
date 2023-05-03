def perfecto(n):
    d = []
    for i in range(1, n):
        if n % i == 0:
            d.append(i)
    if n == sum(d):
        return "{} es perfecto".format(n)
    else:
        return "{} no es perfecto".format(n)


c = int(input())
l = []
for _ in range(c):
    l.append(perfecto(int(input())))

for j in l:
    print(j)
