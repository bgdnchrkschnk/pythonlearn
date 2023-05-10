from enum import Enum
from random import randint
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
        self.id = randint(10000,99999)
        self.account_debet = account_debet

    @property
    def card_kind(self):
        if self.account_debet < 0:
            raise IncorrectDebetError(f"Bank account #{str(self.id)}. \ Debet is under zero: {str(self.account_debet)}")
        elif not self.account_debet:
            return CardsKinds.NO_CARD
        elif self.account_debet > 0 and self.account_debet <= 9000:
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
def say_hello():
    print("hello")


@pytest.fixture
def account_provider():
    return BankSupport

@pytest.fixture
def card_provider():
    return CardsKinds


@pytest.fixture
def check_exception():
    def checker(function, exception: Exception, *args):
        try:
            function(*args)
        except exception:
            return True
        except Exception:
            return False
        return False
    return checker



def test_no_card(account_provider, card_provider):
    assert account_provider(0).card_kind == card_provider.NO_CARD, \
        f"Incorrect type of card has been returned: {card_kind}. Should be {card_provider.NO_CARD}"


def test_normal_card(account_provider, card_provider):
    assert account_provider(1).card_kind == card_provider.NORMAL_CARD, \
        f"Incorrect type of card has been returned: {card_kind}. Should be {card_provider.NORMAL_CARD}"

def test_gold_card(account_provider, card_provider):
    assert account_provider(10001).card_kind == card_provider.GOLD_CARD, \
        f"Incorrect type of card has been returned: {card_kind}. Should be {card_provider.GOLD_CARD}"


def test_platinum_card(account_provider, card_provider):
    assert account_provider(100000).card_kind == card_provider.PLATINUM_CARD, \
        f"Incorrect type of card has been returned: {card_kind}. Should be {card_provider.PLATINUM_CARD}"

def test_negative_debet(account_provider, check_exception):
    assert check_exception(account_provider, IncorrectDebetError, 0), f"Exception IncorrectDebetError hasn't been raised \
     when created account with negative debet {str(-10)}"