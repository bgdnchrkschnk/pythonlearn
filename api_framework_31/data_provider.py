import random
import string

def user_json():
    user_data = {
        "user": {
            "login": f"{random.choices(string.ascii_letters, k=random.randint(1, 10))}",
            "email": "email1326s@gmail.com",
            "password": "pw1326s"
        }
    }