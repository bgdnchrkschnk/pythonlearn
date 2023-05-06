from abc import ABC, abstractmethod

class Beverage(ABC):

    def getDescription(self):
        return f"{self.__class__.__name__}: {self.__class__.DESCRIPTION}"

    @abstractmethod
    def cost():
        pass

    def __call__(self, *args, q=1):
        res = self.cost * q
        adds = []
        for arg in args:
            if isinstance(arg, object):
                res += arg.COST
                adds.append(arg)
        if not adds:
            print(f"Your order is {q} {self.__class__.__name__} coffee. Check: {res} uah")
        else:
            print(f"Your order is {q} {self.__class__.__name__} coffee + adds: {[[add.__name__, add.COST] for add in adds]}. Check: {res} uah")



def with_steamedmilkandmocha(cls):
    def wrapper():
        def withsteamedmilkandmocha(self):
            print(self.__class__.COST + SteamedMilk.COST + Mocha.COST)
        cls.withsteamedmilkandmocha = withsteamedmilkandmocha
        return cls
    return wrapper()


class SteamedMilk:
    DESCRIPTION = f"{__name__} - adding option for your coffee!"
    COST = 5

class SoyMilk:
    DESCRIPTION = f"{__name__} - adding option for your coffee!"
    COST = 8

class Mocha:
    DESCRIPTION = f"{__name__} - adding option for your coffee!"
    COST = 7

class Whip:
    DESCRIPTION = f"{__name__} - adding option for your coffee!"
    COST = 10



@with_steamedmilkandmocha
class DarkRoast(Beverage):
    DESCRIPTION = "The best dark roasted coffee in Ukraine!"
    COST = 50

    @property
    def cost(self):
        return self.COST


class Houseblend(Beverage):
    DESCRIPTION = "The best houseblended coffee in Ukraine!"
    COST = 60

    @property
    def cost(self):
        return self.COST

class Decaf(Beverage):
    DESCRIPTION = "The best decaffeined coffee in Ukraine!"
    COST = 40

    @property
    def cost(self):
        return self.COST



a = DarkRoast()
a(SteamedMilk, Mocha)
a.withsteamedmilkandmocha()
