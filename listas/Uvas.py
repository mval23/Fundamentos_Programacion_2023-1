n = int(input())
res = []


def ideal(m):
    n1, i = 0, 1
    while n1 < m:
        n1 = int((i*(i + 1))/ 2)
        i += 1
    if n1 == m:
        return "Puede ser un racimo ideal"
    else:
        return "No puede ser un racimo ideal"


while n != 0:
    res.append(ideal(n))
    n = int(input())

for j in res:
    print(j)
