from weapon import Weapon
import random


class Robot:
    def __init__(self, name, health, power_level):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon = Weapon("laser", 10)
        self.armory = [Weapon("laser", 10), Weapon("rocket", 15), Weapon("saw", 5)]

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacks {dinosaur.type} with {self.weapon.type} for {self.weapon.attack_power} heath is {dinosaur.health}.")

    def choose_weapon(self):
        return self.armory[random.randint(0, 2)]






