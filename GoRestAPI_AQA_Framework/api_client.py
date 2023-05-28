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

    def _get(self, endp):
        endpoint = self.build_endpoint(endp)
        return self.__client.get(endpoint)

    def _post(self, endp, data):
        endpoint = self.build_endpoint(endp)
        return self.__client.post(url=endpoint, json=data)

    def __head_upd(self):
        header = f"Bearer {self.__api_key}"
        headers = dict()
        headers["Authorization"]=header
        self.__client.headers.update(headers)


    def __del__(self):
        self.__client.close()


a = BasicAPIClient("4ecc7a7f15532f24821f31d2604d0bc69c19562496286a142c554e4f914c2bfb")
print(a._get("/public/v2/users/2204089").json())


