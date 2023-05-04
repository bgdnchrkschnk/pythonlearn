from functools import wraps
import logging
import requests

class post:

    def __init__(self, url:str):
        self.url = url

    def __call__(self, func):
        @wraps(func)
        def wrapper(user_obj:JsonModel):
            request_body = user_obj.as_dict()
            res = requests.post(self.url, headers={"Content-Type":"application/json", "accept": "application/json"}, json=request_body)

            # If HTTP status code is not 200, returning current status code
            if not res.ok:
                print(f"Bad status code: {res.status_code}")
                print(f"Error message: {res.text}")
                return res.status_code, res.text

            # Otherwise returning the result of the function execution
            print(f"Status code is {res.status_code}")
            return func(user_obj)
        return wrapper

import json
from functools import reduce

class get:

    def __init__(self, url, user):
        self.url = url
        self.user = user


    def __call__(self, cls):
        res = requests.get(f"{self.url}/{self.user}", headers={"accept":"application/json"})
        print(f"Response: {res.text}")

        if not res.ok:
            return res.status_code, res.text
        else:
            response = res.json()

            def __init__(self):
                self.__dict__ = {**self.__dict__, **response}
            cls.__init__ = __init__

        return cls


from alchemize import JsonModel,Attr

class User(JsonModel):
    __mapping__ = {
        'user': Attr('user', str),
        'firstName': Attr('first_name', str),
        'lastName': Attr('last_name', str),
        'email': Attr('email', str),
        'phone': Attr('phone', str),
        'password': Attr('password', str),
        'id': Attr('id', int),
        'userStatus': Attr('user_status', int),
    }

    def __init__(self, user, firstName, lastName, email, phone, password, id, userstatus):
        self.user = user
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.phone = phone
        self.password = password
        self.id = id
        self.user_status = userstatus
        print(f"User {self.user} has been successfully created!")

    def __repr__(self):
        return self.user

    def __str__(self):
        return self.user


@post(url="https://petstore.swagger.io/v2/user")
def register_user(user_obj:JsonModel):
    return user_obj

import random
import string

username = ''.join(random.choices(string.ascii_letters, k=10))
password = ''.join(random.choices(string.ascii_letters, k=20))
firstName = ''.join(random.choices(string.ascii_letters, k=10))
lastName = ''.join(random.choices(string.ascii_letters, k=10))
email = f"{''.join(random.choices(string.ascii_letters, k=10))}@hotmail.com"
phone = "12345"
id = 0
userStatus = 0

user = None

if __name__ == "__main__":
    user = register_user(User(username, password, firstName, lastName, email, phone, id, userStatus))
    print(user.first_name, user.last_name, user.id)

    assert isinstance(user, User), f"Username {username} is not registered properly. Status code returned: {user[0]}, Message: {user[1]}"

