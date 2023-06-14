with open('src/cadena.txt', 'r') as file1:
    lines = file1.readlines()


def cadena(l):
    if len(l) == 1:
        return 'cadena completa'
    elif l[0][-2:] == l[1][:2]:
        l.pop(0)
        return cadena(l)
    elif l[0][-3:] == l[1][:3]:
        l.pop(0)
        return cadena(l)
    else:
        return 'cadena rota'


for line in lines:
    print(cadena(line.split()))
