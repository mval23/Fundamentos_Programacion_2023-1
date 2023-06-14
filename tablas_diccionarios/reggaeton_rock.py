n = int(input())
letra1 = []
letra2 = []

for _ in range(n):
    letra1.extend(input().split(' '))

n = int(input())

for _ in range(n):
    letra2.extend(input().split(' '))

s1 = set(letra1)
s2 = set(letra2)
if '' in s2:
    s2.remove('')
if '' in s1:
    s1.remove('')

print('Reggaeton: {} Rock: {}'.format(len(s1), len(s2)))