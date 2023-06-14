goodbye = {
    0: 'Hasta luego curso! Turing, puedes estar orgulloso de mi',
    1: 'Goodbye course! Turing, you can be proud of me',
    2: 'Au revoir cours! Turing, tu peux etre fier de moi',
    3: 'Adeus, curso! Turing, pode se orgulhar de mim',
    4: 'Auf Wiedersehen! Turing, du kannst stolz auf mich sein'
}

n = int(input())

while n > 4:
    print(goodbye.get(n % 5))
    n //= 5

