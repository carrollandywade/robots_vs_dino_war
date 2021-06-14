

class Dinosaur:
    def __init__(self, type, health, energy, attack_power):
        self.type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power


    def set_type(self):
        self.type = input("Enter Dinosaur type:")
        print("Dinosaur type: ", self.type)
