pMax = int(input())
n = int(input())
p = 0
m = 0
for i in range(n):
    p1 = int(input())
    if p + p1 <= pMax:
        p += p1
        m += 1

print("En el ascensor entraron {} personas de la lista con un peso total de {} Kg".format(m, p))

