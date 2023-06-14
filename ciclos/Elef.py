t = float(input())
n = int(input())
c = 0
p2 = 0
for i in range(1, n + 1):
    p1 = float(input())
    p2 += p1
    if p2 > t:
        continue
    c += 1
print(c)
