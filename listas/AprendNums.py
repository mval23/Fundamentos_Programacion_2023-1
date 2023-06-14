n = int(input())
l = []

for i in range(0, n):
    l.append(int(input()))

for i in range(1,6):
    print("{}: {}".format(i, l.count(i)))
