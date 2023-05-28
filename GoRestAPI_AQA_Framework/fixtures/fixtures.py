import pytest
from GoRestAPI_AQA_Framework.api_client import *
from GoRestAPI_AQA_Framework.data_provider import *

@pytest.fixture(scope="session")
def api_client():
    client = BasicAPIClient("4ecc7a7f15532f24821f31d2604d0bc69c19562496286a142c554e4f914c2bfb")
    yield client
    del client


@pytest.fixture
def user_endp():
    return "/public/v2/users/"


@pytest.fixture
def return_data_provider():
    dataprovider = DataProvider()
    return dataprovider()