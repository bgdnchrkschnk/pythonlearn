import json
import requests


def build_endpoint(endpoint, api_key, **kwargs):
    kw = dict(kwargs)
    return f"https://api.openweathermap.org/data/3.0/{endpoint}?{'&'.join([f'{i}={j}' for i,j in zip(kw.keys(), kw.values())])}&appid={api_key}"


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

class CurrentWeatherClient(AbstractApiClient):
    def get_current_weather(self, city, country_code=None, state_code=None):
        q = city
        if state_code:
            q += f',{state_code}'
        if country_code:
            q += f',{country_code}'
        return self._get('weather', q=q)

import pytest

@pytest.fixture(scope="session")
def current_weather_client():
    api_client = CurrentWeatherClient("15bca8c10e86424df00fa826657dca87")
    yield api_client
    del api_client

@pytest.mark.parametrize("city, country_code",[
    ("kyiv", "ua"),
    ("warsaw", "pl"),
    ("berlin", "de")
])
def test_current_weather(self, client:CurrentWeatherClient, city, country_code):
    single_request = client.get_current_weather(city)
    city_current_weather = client.get_current_weather(city, country_code=country_code)

    assert single_request.ok, f"Request failed with the status code {single_city_request.status_code}"
    assert city_current_weather.ok, f"Request failed with the status code {city_current_weather.status_code}"

    assert single_request.json() == city_current_weather.json(), f"""Requests with city and city with country give different results
        With city ({city}) only
        {single_city_request.json()}
        With city and country ({city}, {country_code})
        {city_country_request.json()}"""



