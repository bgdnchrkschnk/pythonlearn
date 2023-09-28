import date_time
from dataclasses import dataclass, field, InitVar, asdict
from abc import abstractmethod
# @dataclass
# class User:
#     login:str
#     sex:str
#     friends : list = field(default_factory=list)
#     env = "dev"
#
#     def __eq__(self, other):
#         return self.login == other.login
#
#
# # u = User("admin","male")
# a = User("moderator","male")
# p = User("patient","female")
# a.friends.append(55)
# print(p.friends)

# @dataclass(init=True, repr=True, eq=True, order=True, frozen=False)
# class Point:
#     x:int
#     y:int
#     z:int
#     calc_len: InitVar[bool] = False
#     lengh:float = field(init=False, repr=True, compare=False, default=0)
#
#     def __post_init__(self, calc_len):
#         if calc_len:
#             self.lengh = (self.x)**2 + (self.y)**2 + (self.z)**2
#
# a = Point(1,2,3)

# from datetime import date
# @dataclass(order=True)
# class Human:
#     name : str = field(compare=False)
#     sex : str = field(compare=False)
#     date : datetime.date = field(compare=False)
#     nationality : str = field(init=False, compare=False, default="Ukrainian")
#     index_sort:int = field(init=False, compare=True)
#
#
#     @property
#     def age(self):
#         self.index_sort = f'{self.name} is {(date.today() - self.date).days // 365} years'
#         return self.index_sort
#
#
# @dataclass(order=True)
# class Man(Human):
#     surname : str = field(compare=False)
#     long : float = field(compare=False, default=15)
#
# @dataclass(order=True)
# class Woman(Human):
#     surname : str = field(compare=False)
#     size : float = field(compare=False)
#
#
# s = Human("Sveta", "female", date(1984, 4, 17))
# print(s.age)
# b = Human("Bogdan", "male", date(1996, 8, 6))
# print(b.age)
# l = [s,b]
# print(sorted(l))

import requests
import json
@dataclass(frozen=True)
class User:
    nickname : str
    sex : str
    age : int
    email : str
    clan : str
a = User("gh0st", "male", 26, "gh0st@ucoz.ru", "In's1de^")
a.age = 17
def default_headers():
    return {
      "accept": "application/json",
      "Content-Type": "application/json"
            }

@dataclass
class Post_request:
    header : dict = field(default_factory=default_headers)

    def post(self, user:User, clas):
        res = requests.post("https://petstore3.swagger.io/api/v3/user", json=asdict(user), headers=self.header)
        print(f"HTTP response code: {res.status_code}\nResponse:{res.text}")
        return clas(res.json())



def create_user(user:User, headers=default_headers):
    test = Post_request()
    return test.post(user, User)

# print(create_user(a))