from datetime import datetime

n = int(input())

# 86400
# hh:mm:ss AM/PM
for _ in range(n):
    t = datetime.strptime(input(), "%I:%M:%S %p")
    load = 0
    load += t.second
    load += t.hour * 3600
    load += t.minute * 60
    load = round(load * 100/86400, 3)
    print('Loading day ... {}%'.format(load))