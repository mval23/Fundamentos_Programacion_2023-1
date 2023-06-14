def congruencia_zeller(d, m, y):
    dias_dict = {
        0: "sabado",
        1: "domingo",
        2: "lunes",
        3: "martes",
        4: "miercoles",
        5: "jueves",
        6: "viernes"
    }
    if m > 12:
        y -= 1
    day = (((d) + ((13*(m + 1))//5) + (y) + ((y)//4) - ((y)//100) + ((y)//400))) % 7
    return dias_dict.get(day)


n = int(input())
meses_dict = {
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
    "enero": 13,
    "febrero": 14
}

for _ in range(n):
    d, m1, y = input().split('-')
    d = int(d)
    m = meses_dict.get(m1)
    y = int(y)
    print(congruencia_zeller(d, m, y))