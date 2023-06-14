n = int(input())
m = int(input())
p = []
wins = []
for i in range(m):
    p.append(int(input()))

for j in range(n):
    wins.append(p.count(j + 1))

for k in range(n):
    if max(wins) == wins[k]:
        print(k + 1)
