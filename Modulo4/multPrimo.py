n = int(input())
l = [2, 3, 5, 7]
m = True

for i in l:
    if n % i == 0 and m:
        print("{} es multiplo de {}".format(n, i))
        m = False

if m:
    print("{} no es multiplo de ninguno de los primeros cuatro primos".format(n))
