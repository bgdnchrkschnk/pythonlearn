import pytest


@pytest.mark.parametrize("user_id", [2191531, 2204089,2191530])
def test_get_users(api_client, user_endp, user_id):
    endpoint = user_endp + str(user_id)
    response = api_client._get(endpoint).json()
    assert user_id in dict(response).values(), f'user {user_id} not found for some reason'

def test_post_user(api_client, user_endp, return_data_provider):
    response = api_client._post(user_endp, data=return_data_provider)
    assert response.ok, f'User has not been created, status code - {response.status_code}'

