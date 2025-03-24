import re
sed = input("Введите дату в формате dd-mm-YYYY: ")

reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-([0-2][0-9][0-9][0-9])"
print(sed)
print(re.findall(reg, sed))