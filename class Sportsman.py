from random import randint

class Sportsman:
    def __init__(self, name:str, agee:int, sport:str, born='Ukraine, Odesa'):
        self.__name = name
        self.__age = agee
        self.__sport = sport
        self.__born = born
        self._lifes = 1
        self.__lucky_number = randint(1,5)

    # @property
    def passport(self):
        if "Ukraine" in self.__born:
            return f"{self.__name} has ukrainian passport, because he was born in {self.__born}"
        elif "Russia" in self.__born:
            return f"{self.__name} has russian passport, because he was born in {self.__born}"

    def run(self):
        return "Run!"

    @property
    def age(self):
        print("Get age")
        return self.__age

    @age.setter
    def age(self, new_age:int):
        if isinstance(new_age, (int,float)):
            self.__age = new_age
            print("Age has been set successfully!")
        else:
            raise ValueError('Please provide a valid age!')

    @age.deleter
    def age(self):
        del self.__age
        print("Age is successfully deleted")

    # age = property(fget=get_age, fset=set_age,fdel=delete_age)

    def print_born(self):
        return f'{self.__name} is from {self.__born}'

    def print_lucky_number(self):
        return f"{self.__name}'s lucky number is {self.__lucky_number}"



kerim = Sportsman("Kerim Musayev", 22, "Muay Thai")
# vertolyot = Sportsman("Nikita Vertolyot", 28, "Footballer")
# usyk = Sportsman("Oleksandr Usyk", 36, "Boxing", born="Ukraine, Simferopol")
# print(kerim.print_born())
# print(kerim.age)
# kerim.age = 55
del kerim.age
print(kerim.age)
# print(usyk.print_born())
# # print(usyk.print_age())
# print(usyk.print_lucky_number())
# islam_mah = Sportsman("Islam Mahachev", 31, "UFC Fighter", born="Russia - Dagestan, Mahachkala")
# print(islam_mah.__dict__)
# print(islam_mah.print_born())
# print(usyk.passport)
# print(islam_mah.passport)
