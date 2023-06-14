with open('src/conversaciones.txt', 'r') as file1:
    lines = file1.readlines()

opositivos = ['SIN EMBARGO', 'NO OBSTANTE', 'AHORA BIEN', 'AUN ASI']

causativos = ['POR TANTO', 'DADO QUE', 'POR CONSIGUIENTE',
              'ASI PUES','POR ENDE']

for line in lines:
    opositivos_c = 0
    causativos_c = 0
    line = line.strip("\n")
    line = line.strip(',')
    line = line.upper()
    for o in opositivos:
        opositivos_c += line.count(o)
    for c in causativos:
        causativos_c += line.count(c)
    print('Opositivos {} Causativos {}'.format(opositivos_c, causativos_c))


