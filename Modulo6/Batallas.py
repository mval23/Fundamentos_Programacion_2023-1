n = int(input())
a, b = [], []
oddness = lambda x: x % 2
s = 0

for i in range(n):
    a.append(int(input()))
a.sort()
for i in range(n):
    b.append(int(input()))
b.sort(reverse=True)
for i in range(n):
    if oddness(a[i]) != oddness(b[i]):
        s += 2

print("Sobreviven {} soldados".format(s))
