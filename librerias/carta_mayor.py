def generador_caso():
    from random import sample
    cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    eleccion = sample(cartas, k=10)
    return eleccion


def juego(humano, plataforma):
    ph = 0
    pp = 0
    for i in range(10):
        if humano[i] > plataforma[i]:
            ph += 1
        elif humano[i] < plataforma[i]:
            pp += 1
    return ph, pp


cantidad = int(input())
for i in range(cantidad):
    humano = generador_caso()
    plataforma = [int(n) for n in input().split()[1:]]
    ph, pp = juego(humano, plataforma)
    print("Puntos humano:", ph, "Puntos plataforma:", pp)