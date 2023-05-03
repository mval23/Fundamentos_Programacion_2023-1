n = int(input())
a = []
b = []
ptsA = 0
ptsB = 0
for i in range(n):
    a.append(int(input()))

for i in range(n):
    b.append(int(input()))

for i in range(n):
    if a[i] == b[i]:
        ptsA += 1
        ptsB += 1
    elif a[i] > b[i]:
        ptsA += 2
    else:
        ptsB += 2

print("Ballenota Futbol Club: {}".format(ptsA))
print("Real Mandril: {}".format(ptsB))
