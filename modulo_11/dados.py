def dados(p):
    h = randint(1, 6) + randint(1, 6)
    if h > p :
        return 'Gana el humano'
    elif p == h:
        return 'Empate'
    else:
        return 'Gana la plataforma'


from random import randint
n = int(input())

for _ in range(n):
    x, p = input(). split(' ')
    print(dados(int(p)))
