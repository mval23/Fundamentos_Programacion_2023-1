n = int(input())
sal = []

while n != 0:
    sal.append(n)
    n = int(input())

sal.sort(reverse=True)
i = round((sal[2] - sal[-3]) / (len(sal) ** 2), 2)
print(i)
