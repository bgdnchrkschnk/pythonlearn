# int
# float
# str
# bool
# list() -
# tuple()
# set() -
# dict = {} -
#
# list = []
# list.append()
#
# tuple = (1,2,3,4,5,6)
import string

# a = list(range(5))
# print(a)

# [print(i)  for i in range(1,11) if not i%2]

# format

# lis = [1,2,3]
#
# def print1(a = []):
#     a.append(a)
#     print(a)
#
# print1(lis)
# print1(lis)
# print1(lis)
#     __new__


# try:
#     print(50)
# except:
#     print(0)
# finally:
#     print("finally")


# class Animal:
#
#     def __init__(self, name, type, age):
#         self.name = name
#         self.type = type
#         self.__age = age
#
#     def __str__(self):
#         return "{0} - {1}".format(self.type,self.name)
#
#     def __set_age(self,value):
#         self.__age = value
#         return self.__age
#
#     def __add__(self, other):
#         if isinstance(other, (int,float)):
#             return self.__age + other
#         if isinstance(other, Animal):
#             return self.__age + other.__age
#
#     def set(self, value):
#         self.__set_age(value)
#
#     def print(self):
#         print(self.name,self.type,self.__age)
#
# karnet = Animal("Karnet","sobaka", 14)
# bobik = Animal("bobik","sobaka", 4)
# print(karnet)
# print(bobik)
# print(karnet+"saf")



#
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def print_age(self):
#         print(self.__age)
#
#     def set_age(self, value:int):
#         if isinstance(value, (int, float)):
#             self.__age = value
#         else:
#             raise ValueErrorError("Please provide valid data!")
#
# a = Human("Andriy", 29)
# a.set_age(32)
# a.print_age()


# lis = [3,2,11,5,6,4,9]
#
# def check_items(expected_number, obj):
#     if len(obj)==expected_number:
#         return "Test passed"
#     else:
#         return f'Test failed - {len(obj)}/{expected_number}'
#
#
# def check_unique(obj):
#     if len(obj) == len(set(obj)):
#         return "Test passed"
#     else:
#         return f'Test failed - {len(obj)} != {len(set(obj))}'
#
#
# print(check_items(7,lis))
# print(check_unique(lis))

# items = [{'name': 'Телевизор LG OLED55A16LA', 'price': 39999, 'old_price': 44999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung QE55Q60AAUXUA', 'price': 28999, 'old_price': 31999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор LG 55UP75006LF', 'price': 17999, 'old_price': 21499, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung UE32T4500AUXUA', 'price': 8699, 'old_price': None, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор LG 43UP75006LF', 'price': 13499, 'old_price': 15999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung UE43AU7100UXUA', 'price': 14599, 'old_price': None, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Kivi 43U710KB', 'price': 10999, 'old_price': 12999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Hisense 55E76GQ', 'price': 19999, 'old_price': 23999, 'promo_label': '−17%'},
#          {'name': 'Телевизор Blaupunkt 65UN265 + Телевизор Blaupunkt 32WB965 в подарок!', 'price': 21999, 'old_price': 25999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Blaupunkt 32FB5000', 'price': 7199, 'old_price': 8999, 'promo_label': '−20%'},
#          {'name': 'Телевизор Gazer TV32-HS2G', 'price': 6599, 'old_price': 7299, 'promo_label': '−10%'},
#          {'name': 'Телевизор Kivi 32F790LW', 'price': 8199, 'old_price': 8999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Bravis LED-24G5000 Smart + T2', 'price': 4099, 'old_price': 4499, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Gazer TV32-HS2G', 'price': 4499, 'old_price': 5999, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Akai UA40LEP1T2S', 'price': 7499, 'old_price': 7799, 'promo_label': '−4%'},
#          {'name': 'Телевизор Hisense 50E76GQ', 'price': 17999, 'old_price': 20999, 'promo_label': '−14%'},
#          {'name': 'Телевизор Akai TV43G21T2', 'price': 6999, 'old_price': 7899, 'promo_label': '−11%'},
#          {'name': 'Телевизор Ergo 43DUS7000', 'price': 9999, 'old_price': 11999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Akai UA32LEZ1T2', 'price': 4899, 'old_price': 5299, 'promo_label': '−8%'},
#          {'name': 'Телевизор Ergo 55WUS9000', 'price': 16299, 'old_price': 16999, 'promo_label': '−4%'},
#          {'name': 'Телевизор Sony KD43X81JR', 'price': 20499, 'old_price': 24999, 'promo_label': 'СУПЕРЦЕНА'},
#          {'name': 'Телевизор Hisense 43A7GQ + Саундбар в подарок!', 'price': 17499, 'old_price': None, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор LG 43UP78006LB', 'price': 14999, 'old_price': 16999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Philips 55PUS7506/12', 'price': 17599, 'old_price': 19799, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Philips 24PFS6805/12', 'price': 6599, 'old_price': None, 'promo_label': None},
#          {'name': 'Телевизор Samsung QE65Q70AAUXUA', 'price': 44999, 'old_price': 49999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung LS32AM700UIXCI/LS32AM700UIXUA', 'price': 11499, 'old_price': 12999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Satelit 43F9100ST', 'price': 6999, 'old_price': 7299, 'promo_label': '−4%'},
#          {'name': 'Телевизор Philips 32PHS6605/12', 'price': 7799, 'old_price': 8399, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Philips 50PUS7506/12', 'price': 15499, 'old_price': 17799, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Blaupunkt 50UN265', 'price': 11999, 'old_price': 16999, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Samsung QE50LS03AAUXUA', 'price': 30999, 'old_price': 38999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Philips 43PUS7506/12', 'price': 12299, 'old_price': 13999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Blaupunkt 32WB965', 'price': 4999, 'old_price': 5699, 'promo_label': '−12%'},
#          {'name': 'Телевизор Akai TV43G21S', 'price': 7999, 'old_price': 8799, 'promo_label': '−9%'},
#          {'name': 'Телевизор Ergo 32DHT5000', 'price': 4999, 'old_price': 6199, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Gazer TV43-US2G', 'price': 13999, 'old_price': 15899, 'promo_label': '−12%'},
#          {'name': 'Телевизор Hisense 32A5710FA', 'price': 6799, 'old_price': 8499, 'promo_label': '−20%'},
#          {'name': 'Телевизор LG 43NANO756PA', 'price': 17499, 'old_price': 19999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung QE50Q60AAUXUA', 'price': 24999, 'old_price': 28999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Sony KD50X81JR', 'price': 25499, 'old_price': 30499, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Philips 65PUS7906/12', 'price': 24599, 'old_price': 33999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Hitachi 32HAE4250', 'price': 7777, 'old_price': 9499, 'promo_label': '−18%'},
#          {'name': 'Телевизор Philips 55PUS7906/12', 'price': 19499, 'old_price': 26999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Nokia Smart TV 4300A', 'price': 11999, 'old_price': 12999, 'promo_label': '−8%'},
#          {'name': 'Телевизор LG OLED65A16LA', 'price': 59999, 'old_price': 64999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Gazer TV24-HS2G', 'price': 5399, 'old_price': 6899, 'promo_label': '−22%'},
#          {'name': 'Телевизор LG 43UP77006LB', 'price': 14299, 'old_price': 16499, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Philips 58PUS8506/12', 'price': 23399, 'old_price': 33999, 'promo_label': '−31%'},
#          {'name': 'Телевизор Samsung UE32T5300AUXUA', 'price': 9999, 'old_price': None, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Samsung UE32T4510AUXUA', 'price': 8699, 'old_price': None, 'promo_label': 'ТОП ПРОДАЖ'},
#          {'name': 'Телевизор Samsung QE43Q60AAUXUA', 'price': 20499, 'old_price': 23999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Philips 50PUS7906/12', 'price': 17599, 'old_price': 24499, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Sony KD50X81JR', 'price': 9499, 'old_price': 10699, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung QE75Q60AAUXUA', 'price': 50999, 'old_price': 59999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор LG 55NANO816PA', 'price': 27999, 'old_price': 29999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор LG 50UP75006LF', 'price': 15699, 'old_price': 19499, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор Samsung QE75QN90AAUXUA', 'price': 123999, 'old_price': None, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор LG 55NANO756PA', 'price': 24999, 'old_price': 27999, 'promo_label': 'АКЦИЯ'},
#          {'name': 'Телевизор LG OLED65C14LB', 'price': 79999, 'old_price': None, 'promo_label': 'АКЦИЯ'}]
#
# res = [item["name"] for item in items]

# def check_be_unique_items(obj):
#     res = [item["name"] for item in obj]
#     result = []
#     if len(res) == len(set(res)):
#         return "Passed"
#     else:
#         for i in set(res):
#             if res.count(i) > 1:
#                 result.append(i)
#         else:
#             return "Failed, options are duplicated on page: ", *result
#
#
# print(check_be_unique_items(items))

# def filter_by_text(text):
#     counter = 0
#     for i in res:
#         if not text in i:
#             counter += 1
#     else:
#         if not counter:
#             return "Passed"
#         else:
#             return "Failed"
#
#
# print(filter_by_text("Телевизор"))

# def divide(a,b):
#     assert b != 0, "You cannot divide on 0!"
#     assert isinstance(a, int), "Invalid data provided!"
#     return a/b
#
# print(divide("6",7))

# import datetime
# def decorator(func):
#     def wrapper():
#         print("Decorator started...")
#         func()
#         print("Decorator finished")
#     return wrapper
#
# @decorator
# def time_is():
#     print(f"Now is {datetime.datetime.now()}")
#
# time_is()

# def dec_x2(func):
#     def wrapper(*args):
#         print("x2:")
#         return func(*args)*2
#     return wrapper
#
#
# @dec_x2
# def pluss(*args):
#     res = 0
#     for i in args:
#         res+=i
#     return res
#
# print(pluss(5,4,1))

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print_title()
#         func(*args, **kwargs)
#     return wrapper
#
#
# def print_title():
#     print("CEO Red Bull Inc.")
#     print("Mr. John Bigbull")
#
#
# @decorator
# def vacation(first_name, surname, from_date, to_date):
#     print(f"Hi John, I need the paid vacations from {from_date} to {to_date}.")
#     print(f"{first_name} {surname}")
#
# @decorator
# def sick_leave(first_name, surname, from_date, to_date):
#     print(f"Hi John, I need the paid sick leave from {from_date} to {to_date}.")
#     print(f"{first_name} {surname}")
#
# @decorator
# def day_off(first_name, surname, from_date, to_date):
#     print(f"Hi John, I need the paid day off from {from_date} to {to_date}")
#     print(f"{first_name} {surname}")
#
# day_off("Bogdan", "Cherkashchenko", "19/03/23", "24/03/23")


# res = {i * 2 for i in range(1,11) if not i%2}
# print(type(res))
# for i in res:
#     print(i)

# keys = [str(i) for i in range(1,11)]
# values = [i for i in range(1,11)]
# my_dict = {k:v for k,v in zip(keys, values)}
# print(my_dict)





# class Human():
#     def __init__(self, name, surname, age, gender):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.gender = gender
#
#     def eat(self):
#         print("eat")
#
#     def sleep(self):
#         print("sleep")
#
#     def speak(self):
#         print("speak")
#
#     def walk(self):
#         print("walk")
#
#     def stand(self):
#         print("stand")
#
#     def lay(self):
#         print("lay")
#
# a = Human("bogdan", "cherkashchenko", 26, "male")
# print(a.__dict__)
# a.speak()

# x = [1,2,3,4,5]
# res = list(filter(lambda x: not x%2, x))
# print(res)

# from functools import reduce
# list = [i for i in range(1,11)]
# res = reduce(lambda x,y: x+y, list)
# print(res)

# class Human:
#     def __init__(self, name:str, age:int):
#         self.name = name
#         self.age = age
#     def breathe(self):
#         print(f"{self.name} is breathing")
# class Singer(Human):
#     def __init__(self, name:str, age:int):
#         super().__init__(f'Singer - {name}', age)
#
# class Dev(Human):
#     def __init__(self, name:str, age:int, stack:str, experience:(int,float)):
#         super().__init__(f"Developer - {name}", age)
#         self.stack = stack
#         self.experience = experience
#     def to_dev(self, stack:str):
#         if stack == self.stack:
#             print(f"{self.name} has started to develop!")
#         else:
#             raise TypeError('This developer does not match with current stack!')
#
# class Footballer(Human):
#     def __init__(self):
#         super().__init__("Nikita Simonyan", 24)
#
#     def breathe(self):
#         print(f"{self.name} is intensively breathing! He is on a match right now!")
#
#
#
# h = Human("bolvan", 15)
# s = Singer("Max Armstrong", 26)
# print(s.name)
# s.breathe()
# d = Dev("Khutor", 26, "JS", 4.5)
# d.breathe()
# d.to_dev("JS")
# print(d.name, "-", d.age)
# f = Footballer()
# f.breathe()
#from abc import ABC, abstractmethod

# class Human():
#     def __init__(self, age):
#         self.age = age
#
#     #@abstractmethod
#     def piss(self):
#         raise NotImplementedError('piss func not implemented!')
#
# class Man(Human):
#     def __init__(self, age, name):
#         super().__init__(age)
#         self.name = name
#
#     def piss(self):
#         print("Pissing via penis")
#
# class Woman(Human):
#     def __init__(self, age, name):
#         super().__init__(age)
#         self.name = name
#
#     def pisss(self):
#         print("Pissing via vagina")
#
# m = Man(26, "Bogdan")
# w = Woman(22, "Diana")
# print(m.__dict__)
# print(w.__dict__)
# m.piss()
# h = Human(15)


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def act(self):
        print(f"act like a parent")

class Friend:
    def __init__(self, name, age, music):
        self.name = name
        self.age = age
        self.music = music

    def act(self):
        print(f"act like a friend")

class Daughter(Parent, Friend):
    STATUS = "Active"
    def __init__(self, name, age, music, sex):
        Parent.__init__(self, name, age)
        Friend.__init__(self, name, age, music)
        self.sex = sex


d = Daughter("daugher", 15, "pop", "female")
print(Friend.act(d))


