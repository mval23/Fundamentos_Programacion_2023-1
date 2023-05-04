def bandera_escocesa(l):
    for row in range(1, l + 1):
        for col in range(1, l + 1):
            if (col == row) or (col == l - (row - 1)):
                print('#', end='')
            else:
                print('0', end='')
        print(end="\n")


n = int(input())
while n != 0:
    bandera_escocesa(n)
    print('')
    n = int(input())
