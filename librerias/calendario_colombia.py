def dias_mes(mes, año):
    mes_con_30 = [4, 6, 9, 11]
    if mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            return 29
        else:
            return 28
    elif mes in mes_con_30:
        return 30
    else:
        return 31


def calendario(d):
    posicion = datetime(d.year, d.month, 1).weekday()
    semana_1 = [1]
    while len(semana_1) != (posicion + 1):
        semana_1.insert(0, "")
    dia = 2
    while len(semana_1) != 7:
        semana_1.append(dia)
        dia += 1
    cals = [["lun", "mar", "mie", "jue", "vie", "sab", "dom"], semana_1]
    semana = []
    for dia in range(dia, dias_mes(d.month, d.year) + 1):
        if len(semana) == 7:
            cals.append(semana)
            semana = []
        semana.append(dia)
    cals.append(semana)
    return cals


from datetime import datetime

n = int(input())
for i in range(n):
    d = datetime.strptime(input(), "%d/%m/%Y")
    cals = calendario(d)
    for i in cals:
        for j in range(len(i) - 1):
            print(i[j], end="\t")
        print(i[-1])
    print('')
