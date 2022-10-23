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

class Cat:
    breed = "Britain"
    def display_breed(instance):
        print(f"My breed is {instance.breed}")
    def show_name(instance):
        if hasattr(instance, "name"):
            print(f"My name is {instance.name}")
        else:
            print("Noname")
    def set_attribute(instance, value):
        instance.name = value
        print("Name is set successfully!")

kokos = Cat()
kokos.display_breed()
kokos.set_attribute("Kokos")
kokos.show_name()


# alisa = Cat()
# alisa.name = "Alisa"
# alisa.show_name()
