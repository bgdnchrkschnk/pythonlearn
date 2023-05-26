import requests


class BasicApiClient:
    base_url = "https://petstore3.swagger.io/api/v2"
    def __init__(self):
        self._api_key = "special_key"
        self._client = requests.Session()

    @property
    def api_key(self):
        return self._api_key

    @staticmethod
    def build_url(endpoint):
        url = BasicApiClient.base_url + endpoint
        return url

    def _get(self, endpoint):
        url = self.build_url(endpoint)
        return self._client.get(url)

    def __del__(self):
        print("Session closed")
        self._client.close()


    def _post(self, endpoint, data):
        url = self.build_url(endpoint)
        print(self._client.post(url, json=data))


