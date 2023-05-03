A = int(input())
B = int(input())

count = 0
serie = [2, 1]

for i in range(B + 1):
    serie.append(serie[-1] + serie[-2])

for i in serie:
    if A <= i <= B:
        count += 1
    elif i > B:
        break

print(count)