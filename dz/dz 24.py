from unicodedata import numeric


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.num = num
        self.surname = surname
        self.persent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

    @property
    def num(self):
        return self.num

    @num.setter
    def num(self, num):
        self.num = num

    @property
    def surname(self):
        return self.surname

    @surname.setter
    def surname(self, surname):
        self.surname = surname

    @property
    def percent(self):
        return self.percent

    @percent.setter
    def percent(self, percent):
        self.percent = percent

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self.value = value

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def set_surname(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname

    def set_percent(self, percent):
        self.percent = percent

    def get_percent(self):
        return self.percent

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.persent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.persent:.0%}")
        print("-" * 20)


acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()
