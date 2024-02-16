line = [2, 8, 10, 13, 17]
line_wods = ['Second line', 'Eighth line', 'Tenth line', 'Thirteenth line', 'Seventeenth line']

with open("lines.txt", "w") as file:
    last_line = max(line)
    line_counter = 1

    while line_counter <= last_line:
        if line_counter in line:
            file.write(f"{line_wods[line.index(line_counter)]}\n")
        else:
            file.write("\n")
        line_counter += 1
