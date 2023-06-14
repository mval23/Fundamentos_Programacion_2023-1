def encadenar(words):
    posicion = words[0].find(words[1][0])
    for i in range(1, len(words[0]) - posicion):
        l1 = words[0][i + posicion]
        l2 = words[1][i]
        if words[0][i + posicion] != words[1][i]:
            return print('False', )
        else:
            aux = i
    phrase = words[0] + words[1][aux + 1:]
    return print('True', phrase)


for line in lines:
    line = line.strip("\n")
    print(encadenar(line.split('-')))