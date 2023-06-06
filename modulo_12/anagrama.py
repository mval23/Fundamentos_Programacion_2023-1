def anagrama(words):
    w1 = words[0].replace(" ", "")
    w2 = words[1].replace(" ", "")
    if sorted(w1) == sorted(w2):
        return "Es anagrama"
    else:
        return "No es anagrama"


n = int(input())
for i in range(n):
    l = input().split(":")
    print(anagrama(l))