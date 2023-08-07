from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name:str, surname:str, age:int):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = None

    @abstractmethod
    def get_money(self):
        pass

    @property
    def balance(self):
        return self.__balance


class Director(Human):
    def __init__(self, name, surname, age, balance:(float,int)=0):
        super().__init__(name, surname, age)
        self.profession = self.__class__.__name__
        self.__balance = balance

    def get_money(self):
            self.__balance += 20000

class Zavuch(Human):
    def __init__(self, name, surname, age, balance:(float,int)=0):
        super().__init__(name, surname, age)
        self.profession = self.__class__.__name__
        self.__balance = balance


    def get_money(self):
            self.__balance += 15000

class Teacher(Human):
    def __init__(self, name, surname, age, balance:(float,int)=0):
        super().__init__(name, surname, age)
        self.profession = self.__class__.__name__
        self.__balance = balance


    def get_money(self):
            self.__balance += 6000


class Student(Human):
    def __init__(self, name, surname, age, balance:(float,int)=0):
        super().__init__(name, surname, age)
        self.profession = self.__class__.__name__
        self.__balance = balance


    def pay_money(self, amount):
            self.__balance -= amount

    def get_money(self, mark:int):
        if mark > 9:
            self.__balance += 100



class School:
    def __init__(self, name):
        self.name = name
        self.__classes = list()

    def add_class(self, clas):
        self.__classes.append(clas)


class Class:
    def __init__(self, name, class_manager:Teacher):
        self.name = name
        self.students = list()
        self.__class_manager = class_manager


    def add_student(self, student:Student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise ValueError("Please add a valid student to a class!")


dima = Student("Dima", "Khutornoy", 26)
vladik = Student("Vlad", "Butnaru", 26)
art = Teacher("Art", "Hz", 26)

a = Class("11-A", art)
a.add_student(dima)
print(a.students)








