def anagrama(words):
    w1 = list(words[0]).sort()
    w2 = list(words[1]).sort()
    if list(w1).sort() == list(w1).sort():
        return "Es anagrama"
    else:
        return "No es anagrama"


l = input().split(":")
print(anagrama(l))