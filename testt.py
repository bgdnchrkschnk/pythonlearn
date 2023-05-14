# x = "besyuwgnjkmbhuynrngejnjknvkiue"
#
# if "e" in x and "b" in x:
#     print("YES")
# else:
#     print("NO")
#
from pytest_lessons.lesson2 import CardsKinds
import random
class DataProvider():
    def __init__(self):
        self.cards = (
            CardsKinds.NO_CARD,
            CardsKinds.NORMAL_CARD,
            CardsKinds.GOLD_CARD,
            CardsKinds.PLATINUM_CARD)

    def __call__(self, normal:int, gold:int, platinum:int):
        norm = (random.randint(1,normal), CardsKinds.NORMAL_CARD)
        gol = (random.randint(normal+1,gold), CardsKinds.GOLD_CARD)
        pl = (random.randint(gold+1,platinum), CardsKinds.PLATINUM_CARD)
        tupl = (norm, gol, pl)
        return tupl

data_provider = DataProvider()
print(data_provider(1,10000,100000))