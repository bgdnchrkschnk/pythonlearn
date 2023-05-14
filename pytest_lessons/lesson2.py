# import pytest
#
# class CalcValueError(Exception):
#     pass
#
#
# def _calculate(a,b):
#     if isinstance(a, (int,float)) and isinstance(b, (int,float)):
#         return a+b
#     else:
#         raise CalcValueError("Invalid value(s) entered")
#
#
# @pytest.fixture
# def calculate():
#     return _calculate
#
# @pytest.mark.parametrize("first_value, second_value, result",[
#     (1,2,3),
#     (-2,1,-1),
#     (-3,-3,-6),
#     # ("a","b", CalcValueError)
# ])
# def test_calculator(calculate, first_value, second_value, result):
#     assert calculate(first_value, second_value) == result
#


from enum import Enum
import random
import pytest

class CardsKinds(Enum):
    NO_CARD = "No Card"
    NORMAL_CARD = "Normal Card"
    GOLD_CARD = "Gold Card"
    PLATINUM_CARD = "Platinum Card"

class IncorrectDebetError(Exception):
    pass

class TakeMoneyUnavailiabilityError(Exception):
    pass




class BankSupport:
    def __init__(self, account_debet=0):
        self.id = random.randint(10000,99999)
        self.account_debet = account_debet

    @property
    def card_kind(self):
        if self.account_debet < 0:
            raise IncorrectDebetError(f"Bank account #{str(self.id)}. \ Debet is under zero: {str(self.account_debet)}")
        elif not self.account_debet:
            return CardsKinds.NO_CARD
        elif self.account_debet > 0 and self.account_debet <= 9999:
            return CardsKinds.NORMAL_CARD
        elif self.account_debet > 10000 and self.account_debet <= 99999:
            return CardsKinds.GOLD_CARD
        else:
            return CardsKinds.PLATINUM_CARD

    def charge_account(self, sum:(int,float)):
        if self.account_debet < 0:
            raise IncorrectDebetError(f"Bank account #{str(self.id)}. \ Debet is under zero: {str(self.account_debet)}")
        elif self.account_debet < sum:
            raise TakeMoneyUnavailiabilityError((f"Bank account #{str(self.id)}. \ Debet is under zero: {str(self.account_debet)}"))
        else:
            self.account_debet -= sum

@pytest.fixture
def check_exception():
    def checker(function, exception: Exception, *args):
        try:
            function(*args).card_kind
        except exception:
            return True
        except Exception:
            return False
        return False
    return checker

@pytest.fixture(autouse=True)
def bank_prov():
    return BankSupport

@pytest.fixture(autouse=True)
def card_prov():
    return CardsKinds

class DataProvider():
    def __call__(self, normal:int, gold:int, platinum:int):
        norm = (random.randint(1,normal), CardsKinds.NORMAL_CARD)
        gol = (random.randint(normal+1,gold), CardsKinds.GOLD_CARD)
        pl = (random.randint(gold+1,platinum), CardsKinds.PLATINUM_CARD)
        tupl = (norm, gol, pl)
        return tupl

data_provider = DataProvider()


# @pytest.mark.parametrize("money, expected_card", [
#     (0, CardsKinds.NO_CARD),
#     (1, CardsKinds.NORMAL_CARD),
#     (10001, CardsKinds.GOLD_CARD),
#     (100000, CardsKinds.PLATINUM_CARD),
#     data_provider(1,10000,100000)
# ])
# def test_cards(money, expected_card, bank_prov):
#     assert bank_prov(money).card_kind == expected_card, f"Incorrect card type returned"


@pytest.mark.parametrize("money, expected_card", data_provider(1,10000,100000))
def test_cards(money, expected_card, bank_prov):
    assert bank_prov(money).card_kind == expected_card, f"Incorrect card type returned"

@pytest.mark.parametrize("func, expected_error, cash",[
    (BankSupport, IncorrectDebetError, -1),
    (BankSupport, IncorrectDebetError, -1000000),
    (BankSupport(10).charge_account, TakeMoneyUnavailiabilityError, 20)
])
def test_negative_card(func, expected_error, cash, check_exception):
    assert check_exception(func, expected_error, cash)


# def test_negative_card(check_exception, bank_prov):
#     assert check_exception(bank_prov, IncorrectDebetError, -10)

