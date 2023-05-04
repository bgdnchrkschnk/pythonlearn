def flying_decorator(cls):
    def wrapper():
        def flying(self):
            print(f"{self} is flying")
        cls.flying = flying
        return cls
    return wrapper()

from abc import ABC, abstractmethod

class Dinosaur(ABC):
    def __init__(self, type):
        self._type = type

    @abstractmethod
    def moving(self):
        pass

    def sleep(self):
        print(f"{self} is sleeping zzZzzzzZz")

@flying_decorator
class Tyranosaur(Dinosaur):
    type = "Tyranosur"
    def __init__(self, type, name:str):
        super().__init__(type)
        self.name = name

    def __repr__(self):
        return f"Tyranosaur {self.name}"

    def __str__(self):
        return f"Tyranosaur {self.name}"

    def moving(self):
        print(f"{self} is moving")

kitty = Tyranosaur("Tyranosaur", "kitty")
print(kitty._type)
kitty.flying()


# def cls_dec(cls):
#         cls.plus = lambda self, num: print(self.number + num)
#         return cls
#
#
# @cls_dec
# class Integer:
#     def __init__(self, number:int):
#         self.number = number
#
#
# one = Integer(1)
# print(one.number)
# one.plus(5)


# def cls_dec(cls):
#     def wrapper():
#         def __init__(self, number:int):
#             self.number = number
#         cls.__init__ = __init__
#         cls.__add__ = lambda self, other : self.number + other.number
#         return cls
#     return wrapper()
#
#
# @cls_dec
# class Integer:
#     def __str__(self):
#         print(self)
#
#
# two = Integer(2)
# three = Integer(3)
# print(two+three)


# def cls_dec(cls):
#    def wrapper():
#        def plus(self, num:int):
#            print(self.number+num)
#        cls.plus = plus
#        return cls
#    return wrapper()
#
#
# @cls_dec
# class Integer:
#    def __init__(self, number:int):
#        self.number = number
#
#
# one = Integer(1)
# one.plus(9)
