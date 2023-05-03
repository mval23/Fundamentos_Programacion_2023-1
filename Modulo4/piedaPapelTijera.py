p1 = input()
p2 = input()
if p1 == p2 :
    print("empate")
elif ((p1 == "piedra") and (p2 == "tijera")) or ((p1 == "tijera") and (p2 == "papel")) or ((p1 == "papel") and (p2 == "piedra")) :
    print("{} vence {}".format(p1, p2))
else:
    print("{} vence {}".format(p2, p1))