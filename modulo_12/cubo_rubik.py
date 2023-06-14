def traspuestas(matriz):
    traspuesta = []
    for i in range(len(matriz)):
        columna = []
        for j in range(len(matriz)):
            columna.append(matriz[j][i])
        traspuesta.append(columna)
    return traspuesta

def creador(dimension):
    cubo = []
    fila = []
    for i in range(1, dimension + 1):
        fila.append(i)
    cubo.append(fila)
    cubo *= dimension
    return cubo

def cambio(cubo, movimiento):
    fila = int(movimiento[1]) - 1
    if movimiento[2] == "+":
        auxiliar = cubo[fila][-1]
        cubo[fila] = cubo[fila][:len(cubo) - 1]
        cubo[fila].insert(0, auxiliar)
        return cubo
    elif movimiento[2] == "-":
        auxiliar = cubo[fila][0]
        cubo[fila] = cubo[fila][1:len(cubo)]
        cubo[fila].append(auxiliar)
        return cubo

cantidad = int(input())
for i in range(cantidad):
    dimension = int(input())
    movimientos = input()
    movimientos = movimientos.split()
    cubo = creador(dimension)
    for movimiento in movimientos:
        if movimiento[0] == "F":
            cubo = cambio(cubo, movimiento)
        elif movimiento[0] == "C":
            traspuesta = traspuestas(cubo)
            traspuesta = cambio(traspuesta, movimiento)
            cubo = traspuestas(traspuesta)
    for i in range(len(cubo)):
        for j in range(len(cubo)):
            print(cubo[i][j], end = "")
        print("")
    print("")