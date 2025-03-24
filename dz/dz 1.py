
a = int(input("Количество студентов"))
students = []
summaas = []
sr = 0
scores = 0
for chi, i in enumerate(range(a),1):
    student = input(f"{chi}-й студент: ")
    summaa = int(input("Бал:"))
    students.append(student)
    summaas.append(summaa)
    sr += summaa
    sredniy_bal = sr / a


student_data = dict(zip(students,summaas))

print("Средний балл",sredniy_bal)

print("Студенты с баллом выше среднего:", )
for key, value in student_data.items():
    if value > sredniy_bal:

        print(key)



