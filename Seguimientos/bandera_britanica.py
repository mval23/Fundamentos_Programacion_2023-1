def bandera(l, matriz):
    for j in range(l):
        for k in range(l):
            if k == j or k == l - 1 - j: # revisar # diagonales
                if matriz[j][k] != "#":
                    return "Ni idea"
            elif j == ((l - 1) / 2) or k == ((l - 1) / 2): # revisar + en la 'mitad'
                if matriz[j][k] != "+":
                    return "Ni idea"
            elif matriz[j][k] != "0": # los otros son ceros
                return "Ni idea"
    return "Bandera britanica"


c = int(input())

for _ in range(c):
    l = int(input())
    matriz = []
    for i in range(l):
        line = input()
        matriz.append(line)
    print(bandera(l, matriz))


