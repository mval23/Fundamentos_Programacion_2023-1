n = int(input())
ventas = {}

for _ in range(n):
    message = input().split(': ')
    alias = message[0]
    quantity = int(message[1])

    if alias in ventas:
        ventas[alias] += quantity
    else:
        ventas[alias] = quantity

winner = max(ventas, key=ventas.get)
print("El vendedor del mes es", winner)