class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды дожны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return x if x > 9 else "0" + str(x)
    #сложение
    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    #вычитание
    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    #умножение
    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    #целочисленное деление
    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    #остаток от деления
    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)



    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    #<
    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec < other.sec

    #<=
    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec <= other.sec

    #>
    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec > other.sec

    #>=
    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec >= other.sec


c1 = Clock(600)
c2 = Clock(200)
c3 = c1 - c2
c4 = c1 * c2
c5 = c1 // c2
c6 = c1 % c2
print(c1.get_format_time())
print(c3.get_format_time())
print(c4.get_format_time())
print(c5.get_format_time())
print(c6.get_format_time())
c1 -= c2
print(c1.get_format_time())
c1 *= c2
print(c1.get_format_time())
c1 //= c2
print(c1.get_format_time())
c1 %= c2
print(c1.get_format_time())

print()

if c1 != c2:
    print("Время одинаковое")
else:
    print("Время разное")

print()

print(f"c3 > c1 {c3 > c1}")
print(f"c3 >= c1 {c3 >= c1}")
print(f"c3 < c1 {c3 < c1}")
print(f"c3 <= c1 {c3 <= c1}")


