from dataclasses import dataclass, field
import random
from enum import Enum
def rand_int():
    return random.randint(1,1000)

class InvalidBalanceError(Exception):
    pass

class DebitCards(Enum):
    FREE_CARD = "FREE CARD"
    GOLD_CARD = "GOLD CARD"
    PREMIUM_CARD = "PREMIUM CARD"

@dataclass
class Card:
    name:str
    gold:bool = field(default=False)
    premium:bool = field(default=False)
    account_id:int = field(init=False, default_factory=rand_int)
    __balance:float = field(init=False, default=0.0)

    def __post_init__(self):
        if not self.premium and not self.gold:
            self.__type = DebitCards.FREE_CARD
        elif self.premium:
            self.__type = DebitCards.PREMIUM_CARD
        elif self.gold:
            self.__type = DebitCards.GOLD_CARD.value
        print(f'Your debit card id: {self.account_id}, type: {self.__type}')



    @property
    def balance(self):
        return f"{self.__balance}$"

    @balance.deleter
    def balance(self):
        del self.__balance

    def charge_balance(self, sum:float):
        if sum <= 0:
            raise ValueError("Invalid value!")
        elif self.__balance < 0:
            raise InvalidBalanceError("Invalid balance for id:", self.account_id)
        else:
            self.__balance += sum
            print(f"Success! Balance: {self.__balance}$")


    def take_balance(self, sum:(float,str)):
        if self.__balance < 0:
            raise InvalidBalanceError("Invalid balance for id:", self.account_id)
        elif sum <= 0:
            raise ValueError("Value error!")
        elif sum>self.__balance:
            raise ValueError("Not enough money on your balance!")
        else:
            self.__balance -= sum
            print(f"Success! Balance: {self.__balance}$")


a = Card("Bogdan", gold=True)
print(a.balance)
