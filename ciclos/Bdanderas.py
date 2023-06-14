l = int(input())
a = int(input())
i = 1
medio_l = (l + 1) / 2
medio_a = (a + 1) / 2
while i <= a:
    if i != medio_a:
        for j in range(1, l + 1):
            if j != medio_l:
                print("0", end='')
            else:
                print("+", end='')
    else:
        for j in range(1, l + 1):
            print("+", end='')
    print(end='\n')
    i += 1



