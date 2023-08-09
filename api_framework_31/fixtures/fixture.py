import pytest
from api_framework_31.api_client import BaseApiClient
from randomuser import RandomUser as users

@pytest.fixture
def session():
    s = BaseApiClient("fb2a1e42cefafa3bdbfcca96e4f691c9")
    yield s
    del s

@pytest.fixture
def get_user():
    login = users().get_username()
    email = users().get_email()
    password = users().get_password()
    user_data = {
            "user": {
                "login": login,
                "email": email,
                "password": password
            }
        }
    return user_data
