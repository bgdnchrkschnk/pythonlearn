import pytest
from GoRestAPI_AQA_Framework.api_client import *
from GoRestAPI_AQA_Framework.data_provider import *

@pytest.fixture(scope="session")
def api_client():
    client = BasicAPIClient("671ee6c260c14819c55da7e1d865032cd2cce86b1c196e477b293a434f19591f")
    yield client
    del client


@pytest.fixture
def user_endp():
    return "/public/v2/users/"


@pytest.fixture
def return_data_provider_user():
    dataprovider = DataProviderUser()
    return dataprovider()

@pytest.fixture
def posts_endpoint():
    return "/public/v2/users/2204089/posts"

@pytest.fixture
def return_data_provider_posts():
    data_provider = DataProviderPosts()
    return data_provider()

@pytest.fixture(scope="session")
def user_client():
    user_client = UsersRequests("671ee6c260c14819c55da7e1d865032cd2cce86b1c196e477b293a434f19591f")
    yield user_client
