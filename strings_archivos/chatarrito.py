def chatarrito_mas_viejo(plates):
    oldest = plates[0]
    for p in plates:
        if oldest > p:
            oldest = p
    if oldest == plates[0]:
        return True
    else:
        return False


n = int(input())

for i in range(n):
    lic_plates = input().split()
    if chatarrito_mas_viejo(lic_plates):
        print('Mi cacharrito es el mas viejo de todos los autos ;D')
    else:
        print('Al menos otro auto es mas viejo que mi cacharrito :(')