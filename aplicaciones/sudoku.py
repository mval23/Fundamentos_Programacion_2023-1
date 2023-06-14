def check_sudoku_line(l):
    for line in l:
        s = len(set(line))
        t = len(line)
        mi = min(line)
        ma = max(line)
        if len(set(line)) != len(line) or min(line) != 1 or max(line) != 9:
            return False
    return True


def traspuesta(matriz):
    t = []
    for i in range(len(matriz)):
        col = []
        for j in range(len(matriz)):
            col.append(matriz[j][i])
        t.append(col)
    return t


n = int(input())

for _ in range(n):
    _ = input()
    sudoku = []
    for _ in range(9):
        line = [int(n) for n in input().split()]
        sudoku.append(line)
    sudoku2 = traspuesta(sudoku)
    if check_sudoku_line(sudoku) == True and check_sudoku_line(sudoku2) == True:
        print('Resuelto')
    else:
        print('No resuelto')
