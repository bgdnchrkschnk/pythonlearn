from api_framework_31.fixtures.fixture import *

def testcase_user_positive(session, get_user):
    response = session._post("users", get_user).json()
    assert "User-Token", "login" in response

def testcase_user_invalid_pw(session):
    login = "user_login_here"
    email = users().get_email()
    password = users().get_password()
    user_data = {
        "user": {
            "login": login,
            "email": email,
            "password": password
        }
    }
    response = session._post("users", user_data)
    assert "Username has already been taken" in dict(response.json()).values(), response.json()
