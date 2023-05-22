import requests
from pprint import pprint

url = "https://4club.com.ua/"
# login_data = {
#     "user_login":"bgdnchrkschnk@gmail.com",
#     "password":"12345qwert"}
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'}

# s = requests.Session()
# response = s.post(url, data=login_data, headers=headers)
# pprint(response.text)


with requests.Session() as http_session:
    http_session.headers.update(headers)
    login_data = {
        "user_login": "bgdnchrkschnk@gmail.com",
        "password": "12345qwert"}
    response = http_session.post(url, json=login_data)
pprint(response.text)