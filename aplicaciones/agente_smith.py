with open("src/matrix.txt", "r") as file:
    lines = file.readlines()

q = []

for line in lines:
    inicio = -1
    fin = -1
    if line.startswith("Smith:"):
        frase = line[len("Smith:"):].strip()

        for i in range(len(frase)):
            char = frase[i]
            if inicio == -1 and char == '?':
                inicio = i
            elif char == '?' and fin == -1:
                fin = i
            pregunta = frase[inicio:fin + 1]
            if fin != -1 and inicio != -1:
                inicio = -1
                fin = -1
                if pregunta not in q and len(pregunta.split()) >= 2:
                    q.append(pregunta)


for question in q:
    print(question.strip())
