file = "text2.txt"
f = open(file,"w")
f.write("Замена строки в текстовом файле;\n"
        "изменить строку в списке;\n"
        "записать список в файл;\n")
f.close()

f = open(file)
read_line = f.readlines()
f.close()

pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
    print("Такой строки нет")
print(read_line)

f = open(file, "w")
f.writelines(read_line)
f.close()