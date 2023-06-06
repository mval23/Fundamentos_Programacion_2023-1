n = int(input())
estudiantes = []

for _ in range(n):
    datos = input().split(", ")
    id = int(datos[0])
    n1 = round(int(datos[1])*5/9, 1)
    n2 = round(int(datos[2])*5/11, 1)
    n3 = round(int(datos[3])*5/12, 1)
    n4 = round(int(datos[4])*5/8, 1)
    n5 = round(int(datos[5])*5/12, 1)
    n6 = round(int(datos[6])*5/9, 1)
    n7 = round(int(datos[7])*5/11, 1)
    n8 = round(int(datos[8])*5/8, 1)
    n9 = round(int(datos[9])*5/11, 1)
    n10 = round(int(datos[10])*5/10, 1)
    n11 = round(int(datos[11])*5/9, 1)
    n12 = round(int(datos[12])*5/10, 1)
    estudiantes.append((id, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12))

definitivas = [(e[0], round(sum(e[1:15])/12, 1)) for e in estudiantes]

definitivas.sort(key=lambda x: x[0])

for e in definitivas:
    print("{} {}".format(e[0], e[1]))



