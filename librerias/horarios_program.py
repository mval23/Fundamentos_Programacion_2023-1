from datetime import datetime


def categorizar_franja_horaria(hora):
    hora_dt = datetime.strptime(hora, '%H:%M:%S')

    if datetime.strptime('00:00:00', '%H:%M:%S') <= hora_dt <= datetime.strptime('03:59:59', '%H:%M:%S'):
        return 'true vampires'
    elif datetime.strptime('04:00:00', '%H:%M:%S') <= hora_dt <= datetime.strptime('07:59:59', '%H:%M:%S'):
        return 'early birds'
    elif datetime.strptime('08:00:00', '%H:%M:%S') <= hora_dt <= datetime.strptime('11:59:59', '%H:%M:%S'):
        return 'sunny warmers'
    elif datetime.strptime('12:00:00', '%H:%M:%S') <= hora_dt <= datetime.strptime('15:59:59', '%H:%M:%S'):
        return 'lunch workers'
    elif datetime.strptime('16:00:00', '%H:%M:%S') <= hora_dt <= datetime.strptime('19:59:59', '%H:%M:%S'):
        return 'sunset lovers'
    elif datetime.strptime('20:00:00', '%H:%M:%S') <= hora_dt <= datetime.strptime('23:59:59', '%H:%M:%S'):
        return 'prime timers'
    else:
        return None


n = int(input())
commits = {
    'true vampires': 0,
    'early birds': 0,
    'sunny warmers': 0,
    'lunch workers': 0,
    'sunset lovers': 0,
    'prime timers': 0
}

for _ in range(n):
    fecha, hora = input().strip().split(' ')
    franja = categorizar_franja_horaria(hora)
    if franja:
        commits[franja] += 1

for key, value in commits.items():
    print('{} {}'.format(key, value))
