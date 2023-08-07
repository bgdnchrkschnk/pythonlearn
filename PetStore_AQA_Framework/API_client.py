import requests
import pytest


def build_url(endpoint):
    url = BasicApiClient.base_url + endpoint
    return url

class BasicApiClient:
    base_url = "https://petstore3.swagger.io/api/v2"
    def __init__(self):
        self._client = requests.Session()


    def _get(self, endpoint):
        url = build_url(endpoint)
        return self._client.get(url)

    def __del__(self):
        print("\nSession closed")
        self._client.close()


    def _post(self, endpoint, data):
        url = build_url(endpoint)
        print(self._client.post(url, json=data))

a = BasicApiClient()
print(a._post("/pet/")

# @pytest.fixture(scope="session")
# def api_client():
#     client = BasicApiClient()
#     yield client
#     del client
#
# # @pytest.mark.parametrize("pet_id",[5, 10])
# def test_get_pet_id(api_client):
#     r = "/pet/" + str(10)
#     endpoint = build_url(r)
#     assert api_client._get("/pet/10").status_code != 500