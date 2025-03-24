def decorate(fn):
    def warp(*arg):
        result = fn(*arg)
        print("Сумма чисел", *arg, "=", result)
        s = len(arg)
        otvet = result % s
        print("Среднее арифметическое число ", *arg, "=", otvet)
        return otvet
    return warp







@decorate
def summa(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(summa(5,9,6,2))