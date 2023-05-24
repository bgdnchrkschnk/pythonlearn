import json
import requests


def build_endpoint(endpoint, api_key, **kwargs):
    kw = dict(kwargs)
    return f"https://api.openweathermap.org/data/3.0/{endpoint}?{'&'.join([f'{i}={j}' for i,j in zip(kw.keys(), kw.values())])}&appid={api_key}"

# print(endpoint("onecall", "biuvb8734g7vghvhjbvrkcfmn874uij5hrf", lat=65))

class AbstractApiClient:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__client = requests.Session()

    @property
    def api_key(self):
        return self.__api_key

    def _get(self, endpoint, **kwargs):
        url = build_endpoint(endpoint, self.__api_key, **kwargs)
        return self.__client.get(url)

    def __del__(self):
        print(f"Session has been deleted successfully!")
        self.__client.close()


odesa = AbstractApiClient("15bca8c10e86424df00fa826657dca87")
print(odesa._get("onecall", lan=76387, lon=8473).status_code)
del odesa


