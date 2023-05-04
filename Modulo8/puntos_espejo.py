def puntos_espejo(l):
    cant = 0
    for i in range(1, len(l)):
        if sum(l[0: i]) == sum(l[i: len(l)]):
            cant += 1
    return cant


n = int(input())
nums = []

for _ in range(n):
    nums.append(float(input()))

print(puntos_espejo(nums))
