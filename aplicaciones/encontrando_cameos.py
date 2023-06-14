def cameos(t):
    cameo = 'saramago'
    t = t.lower()
    c = 0
    while t != '':
        if cameo == '':
            c += 1
            cameo = 'saramago'
        if cameo[0] == t[0]:
            cameo = cameo[1:]
        t = t[1:]
    return c

with open('src/cameos.txt', 'r') as file1:
    lines = file1.readlines()
    for line in lines:
        print(cameos(line))