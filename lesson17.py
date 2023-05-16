from datetime import date
from abc import ABC, abstractmethod
import random


class Human(ABC):

    def __init__(self, name, surname, height, weight, birth_date):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.__children = list()
        self.sex = None
        self.mother = None
        self.father = None

    @property
    def age(self):
        return int(((date.today() - self.birth_date).days) / 365)

    @property
    def children(self):
        return self.__children

    def eat(self, dish):
        print(f"I'm eating {dish}")

    def sleep(self):
        print("I'm sleeping")

    def run(self):
        print("I'm running…")

    @abstractmethod
    def marry(self, partner, marry_partner=True):
        pass

    def add_child(self, child):
        self.__children.append(child)


class Man(Human):

    def __init__(self, name, surname, height, weight, birth_date):
        super().__init__(
            name,
            surname,
            height,
            weight,
            birth_date
        )
        self.sex = "Man"
        self.__wife = None

    @property
    def wife(self):
        return self.__wife

    def fight(self):
        print("Buhh! Bahh! Bahhh!")

    def marry(self, partner, marry_partner=True):
        self.__wife = partner
        if marry_partner:
            self.__wife.marry(self, marry_partner=False)

    def __repr__(self):
        return f"{self.name} {self.surname}"


import datetime


class Woman(Human):

    def __init__(self, name, surname, height, weight, birth_date):
        super().__init__(
            name,
            surname,
            height,
            weight,
            birth_date
        )
        self.sex = "Woman"
        self.__husband = None

    @property
    def husband(self):
        return self.__husband

    def marry(self, partner: Man, marry_partner=True):
        self.__husband = partner
        if marry_partner:
            self.__husband.marry(self, marry_partner=False)

    def birth(self, name, height, weight, father: Man):
        child = random.choice([Man,Woman])(name,father.surname,height,weight, datetime.date.today())
        child.mother = self
        child.father = father

        self.add_child(child)
        father.add_child(child)
        return child

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Androgin(Man, Woman):

    def __init__(self, name, surname, height, weight, birth_date):
        Man.__init__(
            self,
            name,
            surname,
            height,
            weight,
            birth_date)

        Woman.__init__(
            self,
            name,
            surname,
            height,
            weight,
            birth_date)
        self.sex = "Androgin from Enneade"

    def marry(self, partner: Human, marry_partner=True):
        if isinstance(partner, Man):
            self.__husband = partner
            if marry_partner:
                self.__husband.marry(self, marry_partner=False)
        elif isinstance(partner, Woman) or isinstance(partner, Androgin):
            self.__wife = partner
            if marry_partner:
                self.__wife.marry(self, marry_partner=False)

import pytest

@pytest.fixture
def dimas():
    dimas = Man("Dima", "Khutorniy", 170, 60, datetime.date(1996, 10, 17))
    return dimas

@pytest.fixture
def woman_example():
    woman_example = Woman("Nastya", "Karaulan", 165, 55, datetime.date(1996,11,21))
    return woman_example

@pytest.mark.parametrize("testing_date",[
        (datetime.date(2025,10,17)),
        (datetime.date(2026,10,17))])
def test_age_checker(dimas, testing_date):
    assert dimas.age < int(((testing_date - dimas.birth_date).days) / 365)


def test_woman_child_birth(woman_example, dimas):
    child = woman_example.birth("Kolya", 15, 2, dimas)
    assert isinstance(child, Human) and child in dimas.children and child in woman_example.children




