class Student:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.notebook = self.Notebook()


    def show_display(self):
        print(f"{self.name1} => {self.notebook.model}, {self.notebook.processor}, {self.notebook.number}\n"
              f"{self.name2} => {self.notebook.model}, {self.notebook.processor}, {self.notebook.number}")

    class Notebook:
        def __init__(self):
            self.model = "HP"
            self.processor = "i7"
            self.number = "16"

        def show_display(self):
            print(f"модель: {self.model}\nпроцессор {self.processor}\nномер {self.number}")


stud = Student("Roman", "Vladimir")
s = Student.Notebook()
s.show_display()
stud.show_display()