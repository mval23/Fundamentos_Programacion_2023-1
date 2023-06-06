n = int(input())
encuesta = []

for _ in range(n):
    datos = input().split()
    sexo = datos[0]
    edad = int(datos[1])
    percep = datos[2].upper()
    pizza = int(datos[3])
    encuesta.append((sexo, edad, percep, pizza))

positivos = [c for c in encuesta if c[2] == "POSITIVA"]

positivos.sort(key=lambda x: (x[3], x[1]), reverse=True)

for c in positivos:
    print("{} {} {}".format(c[1], c[2], c[3]))



