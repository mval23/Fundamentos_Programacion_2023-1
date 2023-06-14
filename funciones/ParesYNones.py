from math import sqrt

def function(x):
    if x % 2 ==0:
        return sqrt(2 + 5*((4 + x)**3))
    else:
        return (4 + sqrt(2 + 5*x))**3

x = float(input())
l = []
while x != 0:
    l.append(function(x))
    x = float(input())

for j in l:
    print(j)