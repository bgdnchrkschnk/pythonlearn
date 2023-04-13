from abc import ABC, abstractmethod
import random
class Transport:
    mode = None
    def __init__(self, name, mode=mode):
        self.name = name
        self.mode = self.mode

    def start(self):
        print(f"{self.__class__.__name__} started")

    def mode(self):
        print(self.mode)

    def stop(self):
        print(f"{self.__class__.__name__} stopped")


    def moving(self, where:str, distance:int):
        if where in self.__class__.mode and distance:
            return (f"{self.__class__.__name__} moving on {where} with speed {self.max_speed} km/h... The ride will take approximately {distance//self.max_speed} hours")
        else:
            return (f"{self.__class__.__name__} can't move on {where}!")


    def turn(self):
        print(f"{self.__class__.__name__} turning by {self.__class__.rule_by}")

class Car(Transport):
    mode = ["ground"]
    rule_by = "steering wheel"
    max_speed = 140

class Ship(Transport):
    mode = ["water"]
    rule_by = "helm"
    max_speed = 180

class Plane(Transport):
    mode = ["air"]
    rule_by = "plane helm"
    max_speed = 400

class BMP(Car, Ship):
    mode = ["ground", "water"]
    rule_by = "steering wheel"
    max_speed = 120

class Automotive(Car, Plane):
    mode = ["ground", "air"]
    max_speed = 150

c = Car("mercedes")
a = Automotive("tesla")
p = Plane("mriya")
s = Ship("titanik")
b = BMP("tigr")

c.moving("ground", 2000)
c.turn()

my_transport = [c,a,p,s,b]

re = list()
ree = list()
res = list()
[re.append(transport.moving(random.choice(transport.mode), 4500)) for transport in my_transport]
[ree.append(i) for i in (sorted(re, key=lambda x: int(x.split()[-2])))]
[print(el) for el in ree]
