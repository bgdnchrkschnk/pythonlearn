# class Car:
#     model = "BMW"
#     engine = 3.0
#
# a = Car()
#
# print(type(a))
#
# print(isinstance(a, Car))
#
# print(a)


# class Person:
#     name = "Oleg"
#     age = 18

# print(Person.age)
# print(Person.__dict__)
# print(getattr(Person, "name", 100))
#
# Person.age = 21
#
# print(Person.age)

# setattr(Person, "Weight", 75)
# Person.Height = 190
# delattr(Person, "Height")
# print(Person.__dict__)

# a1 = Person()
# a2 = Person()
# a1.name = "Vitaliy"
# a2.name = "Oleksandr"
# print(a1.size)

# class Car:
#     model = "Tesla"
#     year = 2017
#     @staticmethod
#     def create_car():
#         print("Create new car!")
#
# model_s = Car()
#
# model_s.create_car()
# getattr(Car, "create_car")()


# class Cat:
#     breed = "Britain"
#     def display_breed(instance):
#         print(f"My breed is {instance.breed}")

# class Cat:
#     breed = "Britain"
#     def display_breed(instance):
#         print(f"My breed is {instance.breed}")
#
#         def show_name(instance):
#             if hasattr(instance, "name"):
#                 print(f"My name is {instance.name}")
#             else:
#                 print("Noname")
#
#         def set_attribute(instance, value):
#             instance.name = value
#             print("Name is set successfully!")
#
#
# kokos = Cat()
# kokos.display_breed()
# kokos.set_attribute("Kokos")
# kokos.show_name()
# print(f"My breed is {instance.breed}")
#     def show_name(instance):
#         if hasattr(instance, "name"):
#             print(f"My name is {instance.name}")
#         else:
#             print("Noname")
#     def set_attribute(instance, value):
#         instance.name = value
#         print("Name is set successfully!")
#
# kokos = Cat()
# kokos.display_breed()
# kokos.set_attribute("Kokos")
# kokos.show_name()


# alisa = Cat()
# alisa.name = "Alisa"
# alisa.show_name()

# class Car:
#     def __init__(self, model, year, price):
#         self.model = model
#         self.year = year
#         self.price = price
#
# mercedes = Car("cla 180", 2017, "25000$")
# print(mercedes.model)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0,0)
#
#     def print_point(self):
#         print(f"Точка с координатами {self.x},{self.y}")

    # def __str__(self):
    #     return


# p1 = Point()
# print(dict(p1))
# p1.move_to(15,20)
# p1.go_home()
# print(p1.__dict__)
# p1.print_point()

# class Friends:
#     def __init__(self, name, age, job):
#         self.name = name
#         self.age = age
#         self.job = job
#     # def __repr__(self):
#     #     return f"My friend - {self.name}"
#     def __str__(self):
#         return f"Close friend - {self.name}"
#
# fr1 = Friends("Vladik", 26, "3D Animator")
# print(fr1.age)


class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        self.print_tech()

    def print_tech(self):
        print(self.model)
        print(self.year)
        print(self.price)
#

mercedes = Car("cla 180", 2017, "25000$")



