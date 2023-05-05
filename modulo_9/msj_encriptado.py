with open('mensaje.txt', 'r') as file1:
    lines = file1.readlines()

e_lines = []

for line in lines:
    if line == lines[-1]:
        line = line.strip("\n")
        line = line.strip()
        new_line = line[::-1]
    else:
        line = line.strip("\n")
        line = line.strip()
        new_line = line[::-1] + "\n"
    e_lines.append(new_line)

with open('src/mensaje.txt', 'w') as file:
    file.writelines(e_lines)

