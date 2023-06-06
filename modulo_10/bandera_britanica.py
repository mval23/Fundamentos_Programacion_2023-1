def bandera(l):
    dibujo = []
    for i in range(l):
        linea = input()
        dibujo.append(linea)
    for j in range(l):
        for k in range(l):
            if k == j or k == l - 1 - j:
                if dibujo[j][k] != "#":
                    return "Ni idea"
            elif j == ((l - 1) / 2) or k == ((l - 1) / 2):
                if dibujo[j][k] != "+":
                    return "Ni idea"
            elif dibujo[j][k] != "0":
                return "Ni idea"
    return "Bandera britanica"

cantidad = int(input())
for i in range(cantidad):
    l = int(input())
    print(bandera(l))