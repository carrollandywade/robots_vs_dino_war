

class Robot:
    def __init__(self, name, health, power_level, attack_power):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.attack_power = attack_power

    def set_type(self):
        self.name = input("Enter robot name:")
        print("robot name: ", self.name)

