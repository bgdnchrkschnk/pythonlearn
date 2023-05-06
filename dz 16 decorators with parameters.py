# Написати декоратор, котрий приймає в якості параметра число і повертає логічне значення кратності
# результату роботи функції параметру декоратора


import random
#
# class check_multiplicity:
#     def __init__(self, parameter:int):
#         self.parameter = parameter
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result, not result % self.parameter
#         return wrapper
#
#
# @check_multiplicity(3)
# def random_int(fr:int, to:int):
#     return random.randint(fr, to) **2




# Написати декоратор, котрий приймає два параметра: підстрічку, котру треба замінити і підстрічку,
# на яку треба замінити в тексті, котрий згенерує декорована функція.
# Помітьте, що функція, що декорована, має повертати стрічку.

import requests
import string

class word_replace_decorator:
    def __init__(self, rem:str, to:str):
        self.rem = rem
        self.to = to
    def __call__(self, func):
        def wrapper():
            res = func()
            return res.replace(self.rem, self.to)
        return wrapper


@word_replace_decorator("is", "CENSORED")
def get_random_quote():
    __url = "https://raw.githubusercontent.com/ranjith19/random-quotes-generator/master/quotes.txt"
    quotes = requests.get(__url).text.split("\n.\n")
    return random.choice(quotes)


@word_replace_decorator("s", "-CENSORED-")
def generate_string():
    return '' .join(random.choices(string.ascii_letters, k=random.randint(1, 15)))


# print(get_random_quote())
print(generate_string())