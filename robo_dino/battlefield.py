from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run(self):
        self.battlefield_welcome()
        self.introduce_fighters()
        self.battle()

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

    def battle(self):
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs > 0): # while both side are still alive
            self.dino_turn()
            if len(self.fleet.robots) > 0:
                self.robo_turn()

        #loop until one side wins

    def dino_turn(self):

        print("choose dino to attack")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        #choose dino attacker
        #choose dino defender
        #dino attacks robot
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f"{self.herd.dinosaurs[chosen_dino]} has died")
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])

    def robo_turn(self):
        #choose robot attacker
        #choose robot defender
        #robot attacks dino
        pass

    def show_dino_opponent_options(self):
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"{dino.type}")
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        if len(self.fleet.robots) > 0:
            print("robots winner")

