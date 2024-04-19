import pytest


def _calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculate


def test_calc(calculate):
    assert calculate(4, 6) == 10, "Something wrong :/"
