class Human:
    __population = 0

    def __init__(self, name:str, surname:str, age:int, sex:str):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.__plus_one()

    @classmethod
    def __plus_one(cls):
        cls.__population +=1

    @classmethod
    def print_population(cls):
        print(cls.__population)

slavik = Human("Slava", "Zelinsky", 26, "Male")
slavik2 = Human("Slava", "Zelinsky", 26, "Male")
slavik.print_population()