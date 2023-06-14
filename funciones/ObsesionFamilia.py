def F(x):
    if x % 123 == 0:
        return 0
    else:
        return 1 + F(x + 23)

n = int(input())
a = []
for _ in range(n):
    a.append(F(int(input())))

for j in a:
    print(j)
