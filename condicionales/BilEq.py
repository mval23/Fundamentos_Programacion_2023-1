r = int(input())
l = [50000, 20000, 10000, 5000, 2000, 1000]

for i in l:
    if r != 0:
        n = r // i
        if n != 0:
            r -= n * i
            print("{} de ${}".format(n, i))
    else:
        break