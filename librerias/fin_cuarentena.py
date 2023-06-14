from datetime import datetime


def cuarentena(fecha_inicio, fecha_termino):
    inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    termino = datetime.strptime(fecha_termino, '%Y-%m-%d')
    duracion = termino - inicio

    dias = duracion.days
    horas = duracion.days * 24
    minutos = horas * 60
    segundos = minutos * 60

    return f'{dias} dias = {horas} horas = {minutos} minutos = {segundos} segundos'


C = int(input())
for _ in range(C):
    pais, fecha_inicio, fecha_termino = input().split()
    print(cuarentena(fecha_inicio, fecha_termino))
