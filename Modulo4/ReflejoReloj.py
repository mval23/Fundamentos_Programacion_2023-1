h = int(input())
min_0 = int(input())
min_f = 60 - min_0
if min_f == 60:
    min_f = 0
if min_0 == 0:
    h_f = 12 - h
else:
    h_f = (12 - h) - 1
if h_f == 0:
    h_f = 12
elif h_f == -1:
    h_f = 11
print(" {}:{}".format(h_f, min_f))
