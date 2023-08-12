import requests
import os

pw = os.environ["hillel_pw"]
headers = {}
s = requests.Session()

def sign_in():
    endpoint = "https://lms.ithillel.ua/api/lms/users/login"
    r = s.post(url=endpoint, json=dict(email="kebbbbba@gmail.com",password=f"{os.environ['hillel_pw']}"))
    print(r.status_code)
    print(r.json())
    print("-----------------------------")
    s.headers.update(Cookie=r.headers['Set-Cookie'], Referer="https://lms.ithillel.ua/")

def dashboard():
    endpoint = "https://lms.ithillel.ua/api/lms/users/mydata"
    r = s.get(url=endpoint)
    print(r.status_code)
    print(r.json()['response']['first_name'], r.json()['response']['last_name'])

if __name__ == '__main__':
    sign_in()
    dashboard()




