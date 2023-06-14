def camello_serpiente(l):
    snake = ''
    for i in l:
        snake = snake + i.title()
    return snake


n = int(input())

for _ in range(n):
    s = input().split('_')
    print(camello_serpiente(s))
