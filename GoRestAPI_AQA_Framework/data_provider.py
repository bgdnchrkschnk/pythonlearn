import json
import random
import string
import requests

class DataProviderUser:

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

class DataProviderPosts(DataProviderUser):

    def get_random_text(self):
        data = {"LoremType":"Normal",
                "Type":"words",
                "length":"4",
                "__Invariant":"length",
                "X-Requested-With":"XMLHttpRequest"}
        response = requests.post(url="https://randommer.io/Text", data=data)
        return response.text

    def __call__(self):
        title = self.get_random_name()
        body = self.get_random_text()
        data = dict(title=title, body=body)
        return data

