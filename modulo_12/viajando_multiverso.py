def hay_camino(conexion, salto):
    for i in range(len(salto)):
        if salto[i][0] == conexion:
            return salto[i]

cantidad = int(input())
for i in range(cantidad):
    portales = int(input())
    salto = []
    for j in range(portales):
        saltos = input()
        saltos = saltos.split()
        salto.append(saltos)
    camino = salto[0]
    contador = 1
    while camino[1] != "C-137":
        salto.remove(camino)
        camino = hay_camino(camino[1], salto)
        if camino == None:
            print("Deambulan por el multiverso")
            break
        contador += 1
    if camino != None:
        print("Pueden volver a C-137 en", contador, "saltos")