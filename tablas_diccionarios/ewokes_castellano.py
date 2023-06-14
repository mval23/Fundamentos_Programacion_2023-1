N = int(input())
traducciones = {}

for _ in range(N):
    palabra_ewokes, traduccion = input().split()
    traducciones[palabra_ewokes] = traduccion

M = int(input())

for _ in range(M):
    palabra_ewokes = input()
    print(traducciones.get(palabra_ewokes, "palabra no encontrada"))
