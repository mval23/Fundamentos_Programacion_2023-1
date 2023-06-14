from datetime import datetime
c = int(input())
r = []
for i in range(c):
    caso = input().split(", ")
    if caso[1] == "barberia":
        caso[2] = datetime.strptime(caso[2], "%H:%M:%S")
        caso[3] = datetime.strptime(caso[3], "%H:%M:%S")
        r.append(caso[3] - caso[2])
t = 0
for i in r:
    t += i.seconds
p = t / len(r)
h = round(p // 3600)
min = round((p % 3600) // 60)
seg = round((p % 3600) % 60)
print(len(r), "veces")
print(f"{h} horas, {min} minutos, {seg} segundos")