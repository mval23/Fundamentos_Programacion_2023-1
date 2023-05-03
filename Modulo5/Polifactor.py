n = int(input())
num = n
lInf = int(input())
lSup = int(input())
v = True
for i in range(lInf, lSup + 1):
    if n % i != 0:
        v = False
        break
    else:
        n /= i
if v == False:
    print("{} no es polifactor entre {} y {}".format(num, lInf, lSup))
else:
    print("{} es polifactor entre {} y {}".format(num, lInf, lSup))
