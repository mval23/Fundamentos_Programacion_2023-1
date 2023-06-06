def cuadrado_magico(matriz):
    sums = []
    sums.extend(list(map(lambda col: sum(col), zip(*matrix))))



n = int(input())

for _ in range(n):
    x = input()
    for i i