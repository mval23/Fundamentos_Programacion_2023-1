from datetime import datetime
r = int(input())
t1 = datetime.strptime(input(), '%Y-%m-%d %H:%M:%S')
min_p = 0
s_p = 0
h_p = 0
d_p = 0

for _ in range(r - 2):
    t2 = datetime.strptime(input(), '%Y-%m-%d %H:%M:%S')
    dif = t2 - t1
    minutes = dif.seconds // 60
    seconds = dif.seconds % 60
    hours = minutes // 60
    minutes %= 60
    hours %= 24
    t1 = t2
    min_p += minutes
    s_p += seconds
    h_p += hours
    d_p += dif.days
    print('{} dias, {} horas, {} minutos, {} segundos'.format(dif.days, hours, minutes, seconds))


print(format(0))