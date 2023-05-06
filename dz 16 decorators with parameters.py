# Написати декоратор, котрий приймає в якості параметра число і повертає логічне значення кратності
# результату роботи функції параметру декоратора


import random

class check_multiplicity:
    def __init__(self, parameter:int):
        self.parameter = parameter

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result, not result % self.parameter
        return wrapper


@check_multiplicity(3)
def random_int(fr:int, to:int):
    return random.randint(fr, to) **2



import requests
# Написати декоратор, котрий приймає два параметра: підстрічку, котру треба замінити і підстрічку,
# на яку треба замінити в тексті, котрий згенерує декорована функція.
# Помітьте, що функція, що декорована, має повертати стрічку.


class cls_dec:
    def __init__(self,rem:str, to:str):
        self.rem = rem
        self.to = to



__url = "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt"

def get_random_quote():
    quotes = requests.get(__url).text.split("\n.\n")
    return random.choice(quotes)

print(get_random_quote())