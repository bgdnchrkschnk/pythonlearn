import random
import string


class CarShop:
    WHEELS = 4
    TEXTURE = "iron"
    MOST_CHEAP = 0
    MOST_EXPENSIVE = 0
    TOTAL_COUNT = 0
    def __init__(self, model:str, year:int, price:(int,float)):
        self.__model = model
        self.__year = year
        self.__price = price
        self.__article = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(10,100))
        self.__check_price()
        CarShop.TOTAL_COUNT += 1

    def __str__(self):
        return f"{self.__model} ({self.__year}), price {self.__price}$ [{self.__article}]"

    @property
    def price(self):
        return f"{self.__model} ({self.__year}) : {self.__price}$"

    @price.setter
    def price(self, new_value : (int, float)):
        self.__price = new_value
        print(f"Price for {self.__model} has successfully changed for {new_value}$!")

    @price.deleter
    def price(self):
        del self.__price
        print(f"Price status for {self.__model} has changed to Unavailiable")

    def __check_price(self):
        if not CarShop.MOST_EXPENSIVE and not CarShop.MOST_CHEAP:
            CarShop.MOST_EXPENSIVE = self.__price
            CarShop.MOST_CHEAP = self.__price
        elif self.__price > CarShop.MOST_EXPENSIVE:
            CarShop.MOST_EXPENSIVE = self.__price
            print("Wow! This car has marked as most expensive car in our shop!")
        elif self.__price < CarShop.MOST_CHEAP:
            CarShop.MOST_CHEAP = self.__price
            print("Wow! This car has marked as most cheap car in our shop!")

    def get_car_article(self):
        return f"{self.__model} ({self.__year} car article is {self.__article}"

    @classmethod
    def most_price(cls,mode:str):
        if "cheap" in mode:
            return f'The cheapest car in our shop costs {cls.MOST_CHEAP}$!'
        elif "expensive" in mode:
            return f'The most expensive car in our shop costs {cls.MOST_EXPENSIVE}$!'
        else:
            raise ValueError('Please use "cheap" or "expensive" value in mode')

    @classmethod
    def total_count(cls):
        return f"Total count of cars: {cls.TOTAL_COUNT}"

    @staticmethod
    def calculate_price(year:int):
        if 1996 <= year <= 2004:
            print(f"Price will be around 2000-3500$")
        elif year < 1996:
            print(f"Price will be around 600-2000$")
        elif year > 2004:
            print(f"Price will be 3500$+")





lanos1 = CarShop("Daewoo Lanos",2003, 1800)
mers1 = CarShop("Mercedes CLA 180", 2017, 15000)
print(CarShop.total_count())





