
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run(self):
        self.battlefield_welcome()
        self.introduce_fighters()
        self.set_type()

    def battlefield_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def introduce_fighters(self):
        print("here are the fighters:")
        print("Robot: " + self.fleet.robots[0].name)
        print('health is ' + str(int(self.fleet.robots[0].health)))
        print("Robot: " + self.fleet.robots[1].name)
        print('health is ' + str(int(self.fleet.robots[1].health)))
        print("Robot: " + self.fleet.robots[2].name)
        print('health is ' + str(int(self.fleet.robots[2].health)))
        print("Dinosaur: " + self.herd.dinosaurs[0].type)
        print('health is ' + str(int(self.herd.dinosaurs[0].health)))
        print("Dinosaur: " + self.herd.dinosaurs[1].type)
        print('health is ' + str(int(self.herd.dinosaurs[1].health)))
        print("Dinosaur: " + self.herd.dinosaurs[2].type)
        print('health is ' + str(int(self.herd.dinosaurs[2].health)))

    def set_type(self):
        self.type = input("Enter Dinosaur type:")
        print("Dinosaur type: ", self.type)

    def battle(self):


        pass


#    def dino_turn(self):
        pass


#    def robo_turn(self):
        pass


#    def show_dino_opponent_options(self):
        pass


#    def show_robo_opponent_options(self):
        pass


#    def diplay_winners(self):
        pass


