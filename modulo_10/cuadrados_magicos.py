def cuadrado_magico(matriz):

    suma_fila = sum(matriz[0])
    for fila in matriz:
        if sum(fila) != suma_fila:
            return 'Cuadrado muggle'

    for j in range(len(matriz[0])):
        suma_columna = 0
        for i in range(len(matriz)):
            suma_columna += matriz[i][j]
        if suma_columna != suma_fila:
            return 'Cuadrado muggle'

    suma_diagonal_principal = 0
    for i in range(len(matriz)):
        suma_diagonal_principal += matriz[i][i]
    if suma_diagonal_principal != suma_fila:
        return 'Cuadrado muggle'

    suma_diagonal_secundaria = 0
    for i in range(len(matriz)):
        suma_diagonal_secundaria += matriz[i][len(matriz) - 1 - i]
    if suma_diagonal_secundaria != suma_fila:
        return 'Cuadrado muggle'

    return 'Cuadrado magico'


n = int(input())

for i in range(n):
    _ = input()
    m = []
    m.append([int(n) for n in input().split()])
    m.append([int(n) for n in input().split()])
    m.append([int(n) for n in input().split()])
    m.append([int(n) for n in input().split()])
    print(cuadrado_magico(m))
