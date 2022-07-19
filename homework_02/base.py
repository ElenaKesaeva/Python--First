from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=200, fuel=20, fuel_consumption=10):

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):

        if self.fuel > 0:
            self.started = True
            return
        raise LowFuelError("Fuel must be greater than 0")

    def move(self, dist):

        if self.fuel >= dist * self.fuel_consumption:
            self.fuel -= dist * self.fuel_consumption
        else:
            raise NotEnoughFuel("Not enough fuel")


