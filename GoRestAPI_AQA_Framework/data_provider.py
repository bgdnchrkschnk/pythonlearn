import json
import random
import string
import requests

class DataProvider:

    def get_random_name(self):
        response = requests.get(url="https://names.drycodes.com/10?nameOptions=girl_names").text
        resp = response[1:-1].split(",")
        res = random.choice(resp)[1:-1]
        return res

    def __call__(self):
        email = f'{"".join(random.choices(string.ascii_letters, k=random.randint(4,10)))}@{random.choice(["gmail.com", "ukr.net", "mail.ru"])}'
        name = self.get_random_name()
        gender = random.choice(("male", "female"))
        status = "active"
        data = dict(email=email, name=name, gender=gender, status=status)
        return data




# def data_provider(**kwargs):
#     data = {k:v for k, v in dict(kwargs).items()}
#     return data
