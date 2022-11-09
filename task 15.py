# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
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


class Unit:
    def __init__(self, name: str, clan: str, health=100, power=1, skill=1, intelligence=1):
        self.name = name
        self.clan = clan
        self.health = health
        self.power = power
        self.skill = skill
        self.intelligence = intelligence

    def raise_health(self):
        if self.health < 100:
            self.health += 10
        else:
            pass

    def raise_skills(self):
        if isinstance(self, Mage) and self.intelligence < 10:
            self.intelligence += 1
        elif isinstance(self, Archer) and self.arch_type < 10:
            self.arch_type += 1
        elif isinstance(self, Knight) and self.weapon_type < 10:
            self.weapon_type += 1


class Mage(Unit):

    def __init__(self, name, clan, health, power, skill, intelligence, magic_type: str):
        super().__init__(name, clan, health, power, skill, intelligence)
        self.magic_type = magic_type


class Archer(Unit):
    def __init__(self, name, clan, health, power, skill, intelligence, arch_type: str):
        super().__init__(name, clan, health, power, skill, intelligence)
        self.arch_type = arch_type


class Knight(Unit):
    def __init__(self, name, clan, health, power, skill, intelligence, weapon_type: str):
        super().__init__(name, clan, health, power, skill, intelligence)
        self.weapon_type = weapon_type
