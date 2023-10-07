class MyPartner:
    _INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls._INSTANCE:
            return super().__new__(cls)
        else:
            raise Exception("Instance already exists!")

    def __del__(self):
        self.__class__.__INSTANCE = None

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__class__._INSTANCE = self


a = MyPartner("Anya", 21, "Female")
# s = MyPartner("Sveta", 38, "Female")
print(a.__class__._INSTANCE)


# s.__del__()


class A:
    _INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls._INSTANCE:
            return super.__new__(cls)
        else:
            raise Exception("Instance already exists!")

    def __init__(self):
        self.__class__._INSTANCE = self



