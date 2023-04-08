# # from abc import ABC,abstractmethod
# # class Human:
# #     SCHOOL_POPULATION = 0
# #     def __init__(self, name:str,surname:str,age:int,rank:str):
# #         self.name = name
# #         self.surname = surname
# #         self.age = age
# #         self.rank = rank
# #         self.__class__.SCHOOL_POPULATION +=1
# #
# #     @abstractmethod
# #     def get_payment(self):
# #
# # class Personal(Human):
# #     def __init__(self):
# #         pass
# #
# # class Director(Personal):
# #
# #     def get_payment(self):
# #         print("+20000UAH!")
# #
# # class Zavuch(Personal):
# #
# #     def get_payment(self):
# #         print("+15000UAH!")
# #
# class Teacher:
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_payment(self):
#         print("+6000UAH!")
#
# class SchoolClass:
#     def __init__(self, teacher : Teacher):
#         self.teacher = teacher
#
# class Student:
#
#     def __init__(self):
#         pass
#
#
#     def get_payment(self):
#         print("+20000UAH!")
#
#     def compensate(self):
#         print("Payed for services!")
#
# a = SchoolClass(Teacher("lol"))
# print(a.__dict__)


class A:
    def __init__(self, name):
        self.name = name

    def woof(self):
        print("woof!")

class B:
    def __init__(self, age):
        self.age = age

    def woof(self):
        print("woof! woof!")

    def klatc(self):
        print("klatc!")

class C(A,B):

    def __init__(self, name, age):
        A.__init__(self, name)
        B.__init__(self, age)

    def woof(self):
        B.woof(self)

a = C("name", 2)
print(a.age)
