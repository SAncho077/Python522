import math
from abc import abstractmethod

class Shape:
    def __init__(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square0(self):
        pass

    @abstractmethod
    def pain(self):
        pass

    @abstractmethod
    def output(self):
        pass


class Square(Shape):
    def __init__(self, a: int, color: str):
        self.color = color
        self.a = a
        self.ot = None
        self.ot2 = None

    def perimeter(self):
        self.ot = 4 * self.a
        return self.ot

    def square0(self):
        self.ot2 = self.a * self.a
        return self.ot2

    def pain(self):
        for i in range(self.a):
            print("*" * self.a)

    def output(self):
        self.square0()
        self.perimeter()
        print(f"===Квадрат===\nСторона: {self.a}\nЦвет: {self.color}\nПлощадь: {self.ot2}\nПериметр: {self.ot}")
        for i in range(self.a):
            print("*" * self.a)


class Rec(Shape):
    def __init__(self, length: int, width: int, color: str):
        self.color = color
        self.length = length
        self.width = width
        self.get_square = None
        self.get_perimeter = None

    def perimeter(self):
        self.get_perimeter = 2 * (self.length + self.width)
        return self.get_perimeter

    def square0(self):
        self.get_square = self.length * self.width
        return self.get_square

    def pain(self):
        for i in range(self.length):
            print("*" * self.width)

    def output(self):
        self.perimeter()
        self.square0()
        print(f"===Прямоугольник===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\nПлощадь: {self.get_square}\nПериметр: {self.get_perimeter}")
        for i in range(self.length):
            print("*" * self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color
        self.get_square = None
        self.get_perimeter = None

    def perimeter(self):
        self.get_perimeter = self.side1 + self.side2 + self.side3
        return self.get_perimeter

    def square0(self):
        p = (self.side1 + self.side2 + self.side3)/2
        self.get_square = round(math.sqrt((p*(p-self.side1) * (p-self.side2) * (p-self.side3))), 2)
        return self.get_square

    def pain(self):
        for i in range(self.side2):
            print(" " * (self.side2 - i-1) + "*" * (2 * i + 1))

    def output(self):
        self.perimeter()
        self.square0()
        print(f"===Треугольник===\nСторона 1: {self.side1}\nСторона 2: {self.side2}\nСторона 3: {self.side3}\nЦвет: {self.color}\nПлощадь: {self.get_square}\nПериметр: {self.get_perimeter}")
        for i in range(self.side2):
            print(" " * (self.side2 - i - 1) + "*" * (2 * i + 1))


square = Square(3, "red")
square.output()
print()
rec = Rec(3, 7, "green")
rec.output()
print()
tri = Triangle(11,6,6, "yellow")
tri.output()



