# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здoровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

# import random
# class Unit:
#
#     def __init__(self, name, clan):
#         self.name = name
#         self.clan = clan
#         self._health = 100
#         self._power = 1
#         self._skill = 1
#         self._intelligence = 1
#
#
#     def raise_health(self):
#         if self.health < 90:
#             self.health += 10
#         else:
#             self.health = 100
#
#     def raise_skills(self):
#         if isinstance(self, Mage) and self.intelligence < 10:
#             self.intelligence += 1
#         elif isinstance(self, Archer) and self.skill < 10:
#             self.skill += 1
#         elif isinstance(self, Knight) and self.power < 10:
#             self.power += 1
#
#     def __str__(self):
#         return f"Имя - {self.name}, клан - {self.clan}"
#
#
# class Mage(Unit):
#
#     def __init__(self, name, clan):
#         super().__init__(name, clan)
#         self.magic_type = random.choice(["Воздух", "Огонь", "Вода"])
#
#     def __str__(self):
#         return super().__str__() + f", Magic type: {self.magic_type}"
#
# class Archer(Unit):
#     def __init__(self, name, clan):
#         super().__init__(name, clan)
#         self.arch_type = random.choice(["Лук", "Арбалет"])
#
#     def __str__(self):
#         return super().__str__() + f", Magic type: {self.arch_type}"
#
#
# class Knight(Unit):
#     def __init__(self, name, clan):
#         super().__init__(name, clan)
#         self.weapon_type = random.choice(["Меч", "Топор", "Пика"])
#
#     def __str__(self):
#         return super().__str__() + f", Magic type: {self.weapon_type}"
#
#
# mag = Knight("gh0st", "IN'S1DE")
# print(mag.weapon_type)

import random
class Unit:

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self._health = 100
        self._power = 1
        self._skill = 1
        self._intelligence = 1
        self._base_skill = 1


    def increase_skill(self):
        if self._base_skill < 10:
            self._base_skill += 1


    def raise_health(self):
        if self.health < 90:
            self.health += 10
        else:
            self.health = 100


    def __str__(self):
        return f"Имя - {self.name}, клан - {self.clan}"


class Mage(Unit):

    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.magic_type = random.choice(["Воздух", "Огонь", "Вода"])

    def __str__(self):
        return super().__str__() + f", Magic type: {self.magic_type}"

    @property
    def intelligence(self):
        self._intelligence = self._base_skill
        return self._intelligence

class Archer(Unit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.arch_type = random.choice(["Лук", "Арбалет"])

    def __str__(self):
        return super().__str__() + f", Magic type: {self.arch_type}"

    @property
    def skill(self):
        self._skill = self._base_skill
        return self._skill

class Knight(Unit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.weapon_type = random.choice(["Меч", "Топор", "Пика"])

    def __str__(self):
        return super().__str__() + f", Magic type: {self.weapon_type}"

    @property
    def power(self):
        self._power = self._base_skill
        return self._power


hui = Knight("hui", "fucken knights")
print(hui.power)
hui.increase_skill()
hui.increase_skill()
hui.increase_skill()
print(hui.power)
