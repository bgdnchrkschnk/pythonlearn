from enum import Enum, auto

# class DaysOfWeek(Enum):
#     MN = auto()
#     TD = auto()
#     WD = auto()
#     TH = auto()
#     FR = auto()
#     ST = auto()
#     SD = auto()
#
# print(f"Name:{DaysOfWeek.FR.name}, Value:{DaysOfWeek.FR.value}")

class DaysOfWeek(Enum):
    MN = ("Monday", 1)
    TD = ("Tuesday", 2)
    WD = ("Wednesday", 3)
    TH = ("Thursday", 4)
    FR = ("Friday", 5)
    ST = ("Saturday", 6)
    SD = ("Sunday", 7)

    def __init__(self, day, number):
        self.day = day
        self.number = number

    def __str__(self):
        return f"{self.day}, {self.number}"

    def __repr__(self):
        return f"{self.day}, {self.number}"

    def nextday(self):
        if self == self.SD:
            return self.MN
        else:
            return tuple(self.__class__.__members__.values())[self.number]

print(DaysOfWeek.FR.nextday())

print(DaysOfWeek.__members__)
print(DaysOfWeek.__members__.values())



