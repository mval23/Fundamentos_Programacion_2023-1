def dias_naufragio(naufragio, rescate):
    dif = rescate - naufragio
    b = dif.days // 5
    r = dif.days % 5
    bloque = [5] * b
    r = [1] * r
    c = bloque + r
    return c


from datetime import datetime

cantidad = int(input())
for i in range(cantidad):
    caso = input().split()
    caso[0] = datetime.strptime(caso[0], "%d-%m-%Y")
    caso[1] = datetime.strptime(caso[1], "%d-%m-%Y")
    c = dias_naufragio(caso[0], caso[1])
    for j in range(len(c) - 1):
        print(c[j], end=" ")
    print(c[-1])
