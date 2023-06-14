n = int(input('Fibonacci no. '))
l = [0, 1]
for i in range(n - 2):
    l.append(l[-1] + l[-2])

print(l[-1])