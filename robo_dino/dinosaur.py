from weapon import Weapon
import random


class Dinosaur:
    def __init__(self, type, health, energy, attack_power):
        self.type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power
        self.attack_move = (Weapon("claw", 15), Weapon("bite", 20), Weapon("tail", 25))

    def attack(self, robot):
        attack_move = self.choose_attack_move()
        """ parameters: robot = class(robot)"""
        if self.energy >= attack_move.attack_power:
            robot.health -= attack_move.attack_power
            self.energy -= 10
            print(f"{self.type} attacks {robot.name} with {attack_move.type} for {attack_move.attack_power} of damage."
                  f"  New robot heath is {robot.health} and energy is {self.energy}")
        else:
            self.energy += 5
            print("you are too weak to attack, rest for a turn.")

    def choose_attack_move(self):
        print("Choose an attack move")
        self.display_attack_moves()
        chosen_attack_move = int(input())
        return self.attack_move[chosen_attack_move]

    def display_attack_moves(self):
        attack_index = 0
        for attack_move in self.attack_move:
            print(f"Press {attack_index} for {attack_move.type}")
            attack_index += 1

    def __str__(self):
        return self.type
