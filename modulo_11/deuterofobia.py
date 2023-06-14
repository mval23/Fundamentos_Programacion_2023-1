from datetime import datetime


def coincidencia_lunes(n, a):
    c = 0
    for i in range(a):
        n = n.replace(year=n.year + 1)
        if n.weekday() == 0:
            c += 1
    return c


cant = int(input())
for i in range(cant):
    caso = input()
    caso = caso.split()
    caso[0] = datetime.strptime(caso[0], "%Y/%m/%d")
    c = coincidencia_lunes(caso[0], int(caso[1]))
    print(c)
