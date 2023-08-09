import requests


class BaseApiClient():
    base_url = "https://favqs.com/api/"

    def build_endp(self, url):
        return self.base_url + url

    def __init__(self, api_token):
        self.__api_token = api_token
        self._client = requests.Session()
        self.__headers_update()

    def __headers_update(self):
        headers = dict()
        headers["Authorization"] = f"Token token={self.__api_token}"
        # headers['Content-Type'] = "application/json"
        self._client.headers.update(headers)

    def _get(self, url):
        endpoint = self.build_endp(url)
        return self._client.get(url=endpoint)

    def _post(self, url:str, data:dict):
        endpoint = self.build_endp(url)
        #Instead of adding Content-Type: application/json - json=data in request
        return self._client.post(url=endpoint, json=data)



# session = BaseApiClient("")
# response = session._post("users", data)
# print(response.json())