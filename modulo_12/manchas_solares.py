def tiempo(inicio, fin):
    delta = fin - inicio
    dias = delta.days
    horas = delta.seconds // 3600
    minutos = (delta.seconds % 3600) // 60
    segundos = (delta.seconds % 3600) % 60
    return delta, dias, horas, minutos, segundos

from datetime import datetime, timedelta

cantidad = int(input())
caso_1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
contador = timedelta(0, 0, 0)
for i in range(cantidad - 1):
    caso_2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
    delta, dias, horas, minutos, segundos = tiempo(caso_1, caso_2)
    print(f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")
    contador += delta
    caso_1 = caso_2
print()
promedio = contador / (cantidad - 1)
dias = promedio.days
horas = promedio.seconds // 3600
minutos = (promedio.seconds % 3600) // 60
segundos = (promedio.seconds % 3600) % 60
print(f"Promedio: {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")