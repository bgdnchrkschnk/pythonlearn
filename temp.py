import requests
from tools import logg_response

class Api_provider:
    BASIC_URL = "http://translate.google.com"
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__session = requests.Session()

    def _headers_upd(self):
        self.__session.headers.update({"Bearer":self.__api_key})

    def _get(self, endp:str="/", **kwargs):
        url = self.__class__.BASIC_URL + endp
        return self.__session.get(url=url, params=kwargs)

    def _post(self, endp:str="/", data:dict):
        url = self.__class__.BASIC_URL + endp
        return self.__session.post(url=url, data=data)


a = Api_provider("iubfuybhreh784f3")
print(a._get(hl="en", tab="rT", sl="en", tl="uk", text="milk", op="translate").text)



import json
import random
import string


# def get_rand_word(length):
#     alphabet = list(string.ascii_letters)
#     yield random.choice(string.ascii_letters)
#
# print(get_rand_word(5).__next__())

