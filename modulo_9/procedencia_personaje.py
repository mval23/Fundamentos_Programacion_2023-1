origin = {
    'ix': 'Galo',
    'us': 'Romano',
    'ic': 'Godo',
    'as': 'Griego',
    'af': 'Normando',
    'is': 'Breton',
    'ax': 'Breton',
    'ez': 'Hispano',
    'a': 'Indio'
}

n = int(input())
for i in range(n):
    name = input()
    print(origin.get(name[-2:], origin.get(name[-1:], 'Desconocido')))
