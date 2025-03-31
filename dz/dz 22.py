from tkinter.font import names


class Car:

    def __init__(self, name, age, proiz, mosh, color, cena):
        self.name = name
        self.age = age
        self.proiz = proiz
        self.mosh = mosh
        self.color = color
        self.cena = cena

    def print_dano(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.name}\nГод выпуска: {self.age}\nПроизводитель: {self.proiz}\nМощность двигателя: {self.mosh}\n"
              f"Цвет машины: {self.color}\nЦена: {self.cena}")
        print("=" * 40)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_proiz(self, proiz):
        self.proiz = proiz

    def get_proiz(self):
        return self.proiz

    def set_mosh(self, mosh):
        self.mosh = mosh

    def get_mosh(self):
        return self.mosh

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_cena(self, cena):
        self.cena = cena

    def get_cena(self):
        return self.cena


p1 = Car("X7 M50i", "2021", "BMW", "530 л.с", "white", "10790000")
p1.print_dano()
p1.set_age("80")
p1.print_dano()
