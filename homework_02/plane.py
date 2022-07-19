"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane (Vehicle):

    cargo = 0
    max_cargo = 0

    def __init__(self, weight=200, fuel=20, fuel_consumption=10, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if cargo + self.cargo > self.max_cargo:
            raise CargoOverload("Overload")
        self.cargo += cargo

    def remove_all_cargo(self):
        cargo_1 = self.cargo
        self.cargo = 0
        return cargo_1

