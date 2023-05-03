p = int(input())
a = []
c = 0
while p != 0:
    a.append(p)
    p = int(input())
for i in range(len(a)):
    for j in range(i, len(a)):
        if (a[i] + a[j]) == 1995:
            c += 1
print(c)
