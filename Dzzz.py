import random
def cortej(start, end):
    random_number = tuple(random.randint(start, end) for i in range(10))
    return random_number


first = cortej(0,5)
second = cortej(-5,0)
obshiy = first + second
count_0 = obshiy.count(0)

print("Первый кортеж", first)
print("Второй кортеж", second)
print("Третий кортеж", first)
print("Кол-во нулей", count_0)
