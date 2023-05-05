with open('src/trifelios.txt', 'r') as file1:
    lines = file1.readlines()


def trifelio(words):
    phrase = []
    for word in words:
        letters = list(word)
        for l in letters:
            if phrase[-3] == l:




for line in lines:
    line = line.strip("\n")
    print(trifelio(line.split('-'))