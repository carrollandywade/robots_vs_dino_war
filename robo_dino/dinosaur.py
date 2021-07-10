class Dinosaur:
    def __init__(self, type, health, energy, attack_power):
        self.type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power

    def attack(self, robot):
        """ parameters: robot = class(robot)"""
        robot.health -= self.attack_power
        print(f"{self.type} attacks {robot.name} for {self.attack_power} damage.  New heath is {robot.health}.")

