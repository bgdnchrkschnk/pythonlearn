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
from pytest_lazyfixture import lazy_fixture

@pytest.fixture
def dimas():
    dimas = Man("Dima", "Khutorniy", 170, 60, datetime.date(1996, 10, 17))
    return dimas

@pytest.fixture
def vladik():
    return Man("Vlad", "Butnaru", 172, 60, datetime.date(1996, 11, 2))

@pytest.fixture
def woman_example():
    return Woman("Nastya", "Karaulan", 165, 55, datetime.date(1996,11,21))

@pytest.fixture
def woman_example2():
    return Woman("Lolita", "Mochulyak", 163, 65, datetime.date(1996,1,10))

@pytest.fixture
def androgin_example():
    return Androgin("Boris", "Moiseev", 180, 80, datetime.date(1954,3,4))


@pytest.mark.parametrize("testing_date",[
        (datetime.date(2025,10,17)),
        (datetime.date(2026,10,17))])
def test_age_checker(dimas, testing_date):
    assert dimas.age < int(((testing_date - dimas.birth_date).days) / 365)


def test_woman_child_birth(woman_example, dimas):
    child = woman_example.birth("Kolya", 15, 2, dimas)
    assert isinstance(child, Human) and child in dimas.children and child in woman_example.children


def test_child_surname_correct(dimas, woman_example, androgin_example):
    childwoman = woman_example.birth("ch1", 20, 3, dimas)
    childandrogin = androgin_example.birth("ch2", 20, 3, dimas)
    assert childwoman.surname == dimas.surname and childandrogin.surname == dimas.surname

# @pytest.mark.parametrize("mother, father", [
#     ("woman_example", "dimas"),
#     ("woman_example2", "vladik")])
# def test_child_surname(mother:Woman,father:Man, request):
#     mother = request.getfixturevalue(mother)
#     father = request.getfixturevalue(father)
#     child:Human = mother.birth("Slavik", 18, 2, father)
#     assert child.surname == father.surname

@pytest.mark.parametrize("mother, father", [
    (lazy_fixture("woman_example"), lazy_fixture("dimas")),
    (lazy_fixture("woman_example2"), lazy_fixture("vladik"))])
def test_child_surname(mother:Woman,father:Man, request):
    child:Human = mother.birth("Slavik", 18, 2, father)
    assert child.surname == father.surname




