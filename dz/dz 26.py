from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def output(self):
        pass


class Student(Human):
    def __init__(self, name, surname, group, name_group, level):
        super().__init__(name, surname)
        self.group = group
        self.name_group = name_group
        self.level = level

    def output(self):
        return f"{self.name} {self.surname} {self.name_group} {self.name_group} {self.level}"

class Teacher(Human):

    def __init__(self, name, surname, group, name_group, level):
        super().__init__(name, surname)
        self.group = group
        self.name_group = name_group
        self.level = level

    def output(self):
        return f"{self.name} {self.surname} {self.name_group} {self.name_group} {self.level}"

class Graduate(Student):
    def __init__(self, name, surname, group, name_group, level, napravl):
        self.napravl = napravl
        super().__init__(name, surname, group, name_group, level)

    def output(self):
        return f"{self.name} {self.surname} {self.name_group} {self.name_group} {self.level} {self.napravl}"


student = Student("Батодалаев", "Даши", "16", "ГК Wev_001", "5")
print(student.output())
student = Student("Загидуллин", "Линар", "32", "РПО PD_011", "5")
print(student.output())
diplom = Graduate("Шугани", "Сергей", "15", "РПО PD_11", "5", "Защита персональных данных")
print(diplom.output())
t = Teacher("Даньшин", "Андрей", "38", "Астрофизика", "110")
print(t.output())
s = Student("Маркин", "Даниил", "17", "ГК Python_011", "5")
print(s.output())
t = Teacher("Башкиров", "Алексей", "45", "Разработка приложений", "20")