def triangular_superior(m):
    for i in range(1, len(m)):
        for j in range(i):
            if m[i][j] != 0:
                return False
    for i in range(len(m)-1):
        for j in range(i+1, len(m)):
            if m[i][j] != 0:
                return True
    return False

def triangular_inferior(m):
    for i in range(len(m)-1):
        for j in range(i+1, len(m)):
            if m[i][j] != 0:
                return False
    for i in range(1, len(m)):
        for j in range(i):
            if m[i][j] != 0:
                return True
    return False

def diagonal(m):
    for i in range(1, len(m)):
        for j in range(i):
            if m[i][j] != 0:
                return False
    for i in range(len(m)-1):
        for j in range(i+1, len(m)):
            if m[i][j] != 0:
                return False
    return True


cantidad = int(input())
for i in range(cantidad):
    longitud = int(input())
    m = []
    for i in range(longitud):
        fila = input()
        fila = fila.split()
        for j in range(len(fila)):
            fila[j] = float(fila[j])
        m.append(fila)
    if triangular_superior(m):
        print("Triangular superior")
    elif triangular_inferior(m):
        print("Triangular inferior")
    elif diagonal(m):
        print("Diagonal")
    else:
        print("Ni diagonal ni triangular")