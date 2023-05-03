v = int(input())
e = int(input())
d = e - v

print(d)
if (d % 10 == 0 or d % 12 == 0) and d % 7 != 0:
    print("y te lo puedes quedar")