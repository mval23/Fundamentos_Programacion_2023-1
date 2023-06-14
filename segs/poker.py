def escalera(l):
    m = min(l)
    # numeros consecutivos
    if ((m + 1) in l) and ((m + 2) in l) and ((m + 3) in l) and ((m + 4) in l):
        return True
    else:
        return False

def color(l):
    # palo igual
    if l[0] == l[1] and l[0] == l[2] and l[0] == l[3] and l[0] == l[4]:
        return True
    else:
        return False

def escalera_real(l):
    # numeros en la escalera real
    if 10 in l and 11 in l and 12 in l and 13 in l and 14 in l:
        return True
    else:
        return False


n = int(input())

for _ in range(n):
    num = []
    palo = []
    for _ in range(5):
        num.append(int(input()))
        palo.append(input())
    if color(palo) and escalera(num) and escalera_real(num):
        print("Escalera real")
    elif color(palo) and escalera(num):
        print("Escalera de color")
    elif color(palo):
        print("Color")
    elif escalera(num):
        print("Escalera normal")
    else:
        print("Otra mano")







