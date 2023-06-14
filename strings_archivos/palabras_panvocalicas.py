def panvocalica(w, vocals=None):
    if vocals == None:
        vocals = ['a', 'e', 'i', 'o', 'u']
    if len(vocals) == 0:
        return 'Panvocalica'
    elif vocals[-1] in w:
        vocals.pop()
        return panvocalica(w, vocals)
    else:
        return 'No es panvocalica'


n = int(input())

for i in range(n):
    print(panvocalica(input()))
