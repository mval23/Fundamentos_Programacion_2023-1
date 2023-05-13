def trifelio(words):
    w1 = words[1]
    w1 = w1.strip("\n")
    rep = words[0]*2
    if w1 in rep:
        return True
    return False


with open('src/trifelios.txt', 'r') as file1:
    for line in file1:
        if trifelio(line.split("-")):
            print("Es trifelio")
        else:
            print("No es trifelio")

