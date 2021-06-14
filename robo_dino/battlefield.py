
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()


    def run(self):
        self.battlefield_welcome()
        self.introduce_fighters()



    def battlefield_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')




    def introduce_fighters(self):
        print("here are the fighters:")
        print("Robot: " + self.fleet.robots[0].name)
        print("Robot: " + self.fleet.robots[1].name)
        print("Robot: " + self.fleet.robots[2].name)
        print("Dinosaur: " + self.herd.dinosaurs[0].type)
        print("Dinosaur: " + self.herd.dinosaurs[1].type)
        print("Dinosaur: " + self.herd.dinosaurs[2].type)


