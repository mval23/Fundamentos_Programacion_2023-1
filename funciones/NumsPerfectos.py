def Perfectos(n):
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
    if sum(divs) == n:
        return "{} es perfecto".format(n)
    else:
        return "{} no es perfecto".format(n)

c = int(input())
for i in range(c):
    m = int(input())
    print(Perfectos(m))