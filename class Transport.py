from abc import ABC, abstractmethod

class Transport:

    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def moving(self):
        pass
    @abstractmethod
    def turn(self):
        pass

class Car(Transport):
    mode = "ground"
    def start(self):
        print("starting the car")

    def stop(self):
        print("car stopped")

    def moving(self, speed:int, mode=mode):
        if mode == self.__class__.mode:
            print(f"moving on wheels with {speed} km/h")
        elif mode == "water":
            print("drawning in the water :(")
        else:
            raise ValueError('this ground is not supported!')

    def turn(self):
        print("turning by steering wheel")

class Ship(Transport):
    mode = "water"
    def start(self):
        print("starting the ship")

    def stop(self):
        print("ship stopped")

    def moving(self, speed:int, mode=mode):
        if mode == self.__class__.mode:
            print(f"swimming on water with speed {speed} miles/h")
        elif mode == "ground":
            self.stop()
        else:
            raise ValueError('this ground is not supported!')

    def turn(self):
        print("turning by helm")

class Plane(Transport):
    mode = "air"
    def start(self):
        print("starting the plane")

    def stop(self):
        print("plane stopped")

    def moving(self):
        print("flying in air")

    def turn(self):
        print("turning by helm")

class BMP(Car, Ship)