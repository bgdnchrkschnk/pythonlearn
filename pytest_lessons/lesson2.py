import pytest

class CalcValueError(Exception):
    pass


def _calculate(a,b):
    if isinstance(a, (int,float)) and isinstance(b, (int,float)):
        return a+b
    else:
        raise CalcValueError("Invalid value(s) entered")


@pytest.fixture
def calculate():
    return _calculate

@pytest.mark.parametrize("first_value, second_value, result",[
    (1,2,3),
    (-2,1,-1),
    (-3,-3,-6),
    # ("a","b", CalcValueError)
])
def test_calculator(calculate, first_value, second_value, result):
    assert calculate(first_value, second_value) == result

