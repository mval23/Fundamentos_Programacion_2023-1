x = int(input())
n = int(input())
l = []

for i in range(n):
    num = int(input())
    l.append(num) if num % x == 0 else True

print(l)