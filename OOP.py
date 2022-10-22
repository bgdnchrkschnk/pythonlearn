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


class Person:
    name = "Oleg"
    age = 18

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

a1 = Person()
a2 = Person()
a1.name = "Vitaliy"
a2.name = "Oleksandr"
print(a1.size)

