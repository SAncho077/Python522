import math
print("Выбор фигуры",
      "\n1 - треугольник",
      "\n2 - прямоугольник",
      "\n3 - круг")
vvod = int(input(": "))


def otvet2():
    a = int(input("Выберите сторону a: "))
    b = int(input("Выберите сторону b: "))
    return a*b


def otvet3():
    radius = int(input("Введите радиус: "))
    return (math.pi * (radius ** 2))



def otvet1():
    a = int(input("Выберите сторону а: "))
    b = int(input("Выберите сторону b: "))
    c = int(input("Выберите сторону c: "))
    p = (a + b + c) / 2
    okr = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return okr


if vvod == 2:
    print(otvet2())
elif vvod == 3:
    print(otvet3())
elif vvod == 1:
    print(otvet1())