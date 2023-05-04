def divisors(n):
    divs = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divs += 1
    return divs


def julianchi(n):
    """
    El primer elemento de la serie es el número 1
    Cada elemento es igual al elemento anterior más la cantidad
    de divisores de ese elemento anterior
    :param n:
    :return: si hacen o no parte de la serie
    """
    julianchi_nums = [1]
    julianchi_divs = [1]
    i = 0

    while n > julianchi_nums[i]:
        julianchi_nums.append(julianchi_divs[i] + julianchi_nums[i])
        julianchi_divs.append(divisors(julianchi_nums[i + 1]))
        i += 1

    if n in julianchi_nums:
        return 'Pertenece a la serie de Julianachi'
    else:
        return 'No pertenece a la serie de Julianachi'


n = int(input())
while n != 0:
    print(julianchi(n))
    n = int(input())
