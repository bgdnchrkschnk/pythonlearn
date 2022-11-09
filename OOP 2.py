class Human:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Hello, my name is {self.name}, i am {self.age} years old! This month i've earned {self.salary} Keep going!"

    def can_breath(self):
        print("I can breath!")
    def can_eat(self):
        print("I can eat!")
    def can_speak(self):
        print("I can speak!")

    def can_develop(self):
        raise NotImplementedError

class Videoperator(Human):
    def can_rec(self):
        print("I can record!")

class Developer(Human):
    def can_develop(self):
        print("I can develop!")

class Singer(Human):
    def __init__(self, name, age, salary, genre):
        super().__init__(name, age, salary)
        self.genre = genre
    def can_sing(self):
        print("I can sing!")
    def __str__(self):
        return super().__str__() + f" I am making {self.genre}!"

dima = Developer("Dmytriy Khutornoy", 26, "1700$")
milan = Singer("Bogdan Cherkashchenko", 26, "1850EUR", "Pop music")
print(milan)
vlad = Videoperator("Vladislav Butnaru", 26, "500$")
tank = Human("Aleksandr Tanklevskiy", 25, "400$")

print(vlad)
print(issubclass(Singer, Human))
print(isinstance(dima, Singer))

