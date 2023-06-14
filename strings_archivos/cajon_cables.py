def cables_circle(l):
    if l.count('M') == l.count('F'):
        return 'Es posible hacer un unico circulo'
    else:
        return 'No es posible'

n = int(input())

for i in range(n):
    print(cables_circle(input()))