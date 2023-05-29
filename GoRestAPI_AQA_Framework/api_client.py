import requests

class BasicAPIClient:
    basic_url = "https://gorest.co.in"
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__client = requests.Session()
        self.__head_upd()


    def build_endpoint(self, endp):
        endpoint = self.basic_url + str(endp)
        return endpoint

    def _get(self, endp, **kwargs):
        endpoint = self.build_endpoint(endp)
        return self.__client.get(endpoint, params=kwargs)

    def _post(self, endp, data):
        endpoint = self.build_endpoint(endp)
        return self.__client.post(url=endpoint, data=data)

    def _put(self, endp, data):
        endpoint = self.build_endpoint(endp)
        return self.__client.put(url=endpoint, data=data)


    def __head_upd(self):
        header = f"Bearer {self.__api_key}"
        headers = dict()
        headers["Authorization"]=header
        self.__client.headers.update(headers)


    def __del__(self):
        print("Session closed!")
        self.__client.close()

