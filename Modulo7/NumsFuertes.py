def Fuertes(n):
    l = list(str(n))
    sum = 0
    for i in l:
        sum += Factorial(int(i))
    if n == sum:
        return "{} es fuerte".format(n)
    else:
        return "{} no es fuerte".format(n)

def Factorial(a):
    if a == 0:
        return 1
    else:
        return a * Factorial(a - 1)



c = int(input())
for i in range(c):
    m = int(input())
    print(Fuertes(m))