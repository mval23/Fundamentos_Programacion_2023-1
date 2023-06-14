def asesino_serial(dates):
    for i in range(len(dates) - 2):
        if (dates[i + 1] - dates[i]) != (dates[i + 2] - dates[i + 1]):
            return False
    d = dates[1] - dates[0]
    dias_d = d.days
    fecha = dates[-1] + d
    return dias_d, fecha


from datetime import datetime
cantidad = int(input())
for i in range(cantidad):
    caso = input()
    caso = caso.split(", ")
    name = caso[0]
    r = int(caso[1])
    dates = []
    for j in range(r):
        dates.append(datetime.strptime(input(), "%Y-%m-%d"))
    if asesino_serial(dates):
        d = dates[1] - dates[0]
        dias_d = d.days
        fecha = dates[-1] + d
        fecha_final = fecha.strftime("%Y-%m-%d")
        print(name, 'ataca cada', dias_d, 'dias y volvera a hacerlo en', fecha_final)
    else:
        print(name, 'no es asesino(a) serial periodico')
    if i != cantidad - 1:
        print('')