def numeros_armstrong(m):
    l = list(str(m))
    l1 = []
    for i in l:
        l1.append(int(i) ** len(l))
    if sum(l1) == m:
        return '{} es Armstrong'.format(m)
    else:
        return '{} no es Armstrong'.format(m)


n = int(input())
for i in range(n):
    n = int(input())
    print(numeros_armstrong(n))
