def multidigit(s, i=5):
    if i == 0:
        return print('Multidigito')
    elif s.find(str(i)) == -1:
        return print('No es multidigito')
    else:
        return multidigit(s, i - 1)


n = input()

while n != '0':
    multidigit(n)
    n = input()
