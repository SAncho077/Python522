class kg_fund:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return f"{self.__x}кг => {round(self.__x * 2.2, 3)}фунтов"

    @staticmethod
    def _chec(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @x.setter
    def x(self, x):
        if kg_fund._chec(x):
            self.__x = x
        else:
            print("Килограммы задаются только с числами")




p1 = kg_fund(55)
print(p1.x)


