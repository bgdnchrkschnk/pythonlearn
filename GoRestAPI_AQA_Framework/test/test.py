import pytest
import pytest_check as check
from GoRestAPI_AQA_Framework.api_client import *

@pytest.mark.users
@pytest.mark.parametrize("user_id", [2257480, 2204089, 2250467])
def test_get_users(api_client, user_endp, user_id, user_client):
    endpoint = user_endp + str(user_id)
    # response = api_client._get(endpoint).json()
    response = user_client.get(user_id).json()
    print(response)
    assert user_id in dict(response).values(), f'user {user_id} not found for some reason'
    for status in BasicAPIClient.UserStatuses:
        check.is_in(status.value, dict(response).keys())

@pytest.mark.users
def test_post_user(api_client, user_endp, return_data_provider_user, user_client):
    # response = api_client._post(user_endp, data=return_data_provider_user)
    response = user_client.post(data=return_data_provider_user)
    check.is_true(response.ok, f"Fail - {response.json()}")
    assert response.ok, f'User has not been created, status code - {response.status_code}'

def test_create_post(api_client, posts_endpoint, return_data_provider_posts):
    response = api_client._post(posts_endpoint, data=return_data_provider_posts)
    assert response.ok, f"{response.json()}"

@pytest.mark.users
def test_put_user(api_client, user_endp, return_data_provider_user):
    response = api_client._put(user_endp+"2257480", data=return_data_provider_user)
    assert response.ok