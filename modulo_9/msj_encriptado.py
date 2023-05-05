with open('src/mensaje.txt', 'r') as file1:
    lines = file1.readlines()

e_lines = []

for line in lines:
    if "\n" in line:
        new_line = line[-2::-1]
    else:
        new_line = line[::-1]
    e_lines.append(new_line)

for line in e_lines:
    print(line)

