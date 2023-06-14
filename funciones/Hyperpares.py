def Hyperpar(m):
    l = list(str(m))
    l1 = []
    for i in l:
        l1.append(int(i) % 2 == 0)
    if False in l1:
        return "No es hyperpar"
    else:
        return "Hyperpar"


n = int(input())
t = []
while n != -1:
    t.append(Hyperpar(n))
    n = int(input())

for j in t:
    print(j)
