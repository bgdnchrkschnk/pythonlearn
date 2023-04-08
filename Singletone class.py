class MyPartner:
    __INSTANCE = 0

    def __new__(cls, *args, **kwargs):
        if not cls.__INSTANCE:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE

    def __del__(self):
        self.__class__.__INSTANCE = None

    def __init__(self, name, age, sex, **kwargs):
        self.name = name
        self.age = age
        self.sex = sex



a = MyPartner("Anya", 21, "Female")
s = MyPartner("Sveta", 38, "Female")
s.__del__()
print(s)