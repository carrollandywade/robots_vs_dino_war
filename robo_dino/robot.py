from weapon import Weapon
import random


class Robot:
    def __init__(self, name, health, power_level):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon = Weapon("drill", 10)
        self.armory = [Weapon("laser", 15), Weapon("rocket", 20), Weapon("arc blaster", 25)]

    def attack(self, dinosaur):
        armory_weapon = self.choose_weapon()
        if self.power_level >= armory_weapon.attack_power:
            dinosaur.health -= armory_weapon.attack_power
            self.power_level -= 10
            print(f"{self.name} attacks {dinosaur.type} with {armory_weapon.type} for {armory_weapon.attack_power}"
                  f" new dinosaur heath is {dinosaur.health}.")
        else:
            self.power_level += 5
            print("your power level is too low to attack, recharge power banks this turn.")

    def choose_weapon(self):
        print("Choose an attack move")
        self.display_armory_weapons()
        chosen_armory_weapon = int(input())
        return self.armory[chosen_armory_weapon]

    def display_armory_weapons(self):
        weapon_index = 0
        for armory_weapon in self.armory:
            print(f"Press {weapon_index} for {armory_weapon.type}")
            weapon_index += 1

    def __str__(self):
        return self.name


