from PetStore_AQA_Framework.API_client import *
import pytest

@pytest.fixture
def api_client():
    client = BasicApiClient()
    headers = {'accept': 'application/json',
               'Content-Type: application/json'}
    client._client.headers.update(headers=headers)
    yield client
    del client