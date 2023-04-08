class Human:
    __POPULATION = 0
    def __init__(self, name:str, age:int, sex:str):
        self.__name = name
        self.__age = age
        if isinstance(sex, str):
            if sex == "male" or sex == "female":
                self.__sex = sex
            else:
                raise ValueError('Please enter valid data! Use "male" or "female" value')
        else:
            raise TypeError('Please, enter str data!')
        self.__plus_one()
        self._hello(name)

    def __repr__(self):
        return 'The human - {}, {} years old'.format(self.__name, self.__age)

    def _get_name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_value:int):
        self.__age = new_value
        print(f'New age has been successfully set')

    @age.deleter
    def age(self):
        del self.__age
        print(f'Age has been successfully deleted')

    @classmethod
    def __plus_one(cls):
        cls.__POPULATION += 1

    @classmethod
    def get_population(cls):
        return cls.__POPULATION

    @staticmethod
    def _hello(name):
        print('Hello, '+name+". Glad to see you!")

class Worker(Human):
    __PROFESSIONS_TOTAL = 0

    def __init__(self, name:str, age:int, sex:str, profession:str):
        super().__init__(name, age, sex)
        self.__profession = profession
        self.__class__.__PROFESSIONS_TOTAL += 1

    def __repr__(self):
        return 'The {} - {}, {} years old'.format(self.__profession, self._get_name(), self.age)

    def introduce(self, pos_or_neg: str):
        if pos_or_neg == "pos":
            print(
                f'Hello to everyone! My name is {self._get_name()}, I am {self.__profession}, {self.age} y.o. Im so happy be here!')
        elif pos_or_neg == "neg":
            print(f'wassup buddies, i am {self._get_name()}, i am fucking {self.__profession}, when this shit ends?')
        else:
            raise ValueError("Please provide a valid data")

    @classmethod
    def get_total_profs(cls):
        return cls.__PROFESSIONS_TOTAL










b = Human("Bogdanchik", 26, "male")
c = Worker("Dmytro Khutornyi", 26, "male", "Junior JS Developer")
c = Worker("Alexandr Makarov", 28, "male", "Fitness trainer")
c.introduce("pos")
print(c.get_total_profs())





