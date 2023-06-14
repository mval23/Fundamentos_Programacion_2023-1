n = int(input())
nac = 0
for i in range(1, n + 1):
    prom = float(input())
    nacDia = (prom * i) - nac
    nac += nacDia
    print(int(nacDia))
