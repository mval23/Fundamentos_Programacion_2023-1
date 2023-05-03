def escalera(l):
    m = min(l)
    if ((m + 1) in l) and ((m + 2) in l) and ((m + 3) in l) and ((m + 4) in l):
        return True
    else:
        return False


def color(p):
    if p[0] == p[1] and p[0] == p[2] and p[0] == p[3] and p[0] == p[4]:
        return True
    else:
        return False


def imperial(l):
    if (11 in l) and (12 in l) and (13 in l) and (14 in l):
        return True
    else:
        return False


n = int(input())
nums = []
palos = []
r = []
for _ in range(n):
    num = []
    palo = []
    for i in range(5):
        num.append(int(input()))
        palo.append(input())
    nums.append(num)
    palos.append(palo)

for j in range(n):
    if color(palos[j]) and escalera(nums[j]) and imperial(nums[j]):
        print("Flor Imperial")
    elif color(palos[j]) and escalera(nums[j]):
        print("Escalera de Color")
    elif color(palos[j]):
        print("Color")
    elif escalera(nums[j]):
        print("Escalera Normal")
    else:
        print("Otra mano")
