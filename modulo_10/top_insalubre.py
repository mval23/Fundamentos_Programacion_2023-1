n = int(input())
encuesta = []

for _ in range(n):
    datos = input().split(", ")
    nombre = datos[0]
    peso = float(datos[1])
    estatura = float(datos[2])
    azucar = float(datos[3])
    trigl = float(datos[4])
    imc = round((peso/(estatura ** 2)), 1)
    encuesta.append((nombre, peso, estatura, azucar, trigl, imc))

insalubres = [e for e in encuesta if e[5] > 25 and e[3] > 100 and e[4] > 150]

insalubres.sort(key=lambda x: (x[5], x[0]), reverse=True)

i = 0
for c in insalubres:
    i += 1
    print("{} {} {}".format(i, c[0], c[5]))



