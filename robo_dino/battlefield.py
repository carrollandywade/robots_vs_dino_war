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
        self.display_winners()

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
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
            self.dino_turn()
            if len(self.fleet.robots) > 0:
                self.robo_turn()

        #loop until one side wins

    def dino_turn(self):
        print("Choose a dinosaur to unleash")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        print("Choose a target for dinosaur to attack")
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        self.herd.dinosaurs[chosen_dino].attack(self.fleet.robots[chosen_robot])
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f"{self.fleet.robots[chosen_robot]} has been destroyed!")
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])

    def robo_turn(self):
        print("Choose a robot to program")
        self.show_robo_opponent_options()
        chosen_robot = int(input())
        print("Program a target for robot to acquisition")
        self.show_dino_opponent_options()
        chosen_dino = int(input())
        self.fleet.robots[chosen_robot].attack(self.herd.dinosaurs[chosen_dino])
        if self.herd.dinosaurs[chosen_dino].health <= 0:
            print(f"{self.fleet.robots[chosen_dino]} has been exterminated.")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[chosen_dino])

    def show_dino_opponent_options(self):
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f"{dino_index} for {dino.type}")
            dino_index += 1

    def show_robo_opponent_options(self):
        robot_index = 0
        for robot in self.fleet.robots:
            print(f"{robot_index} for {robot.name}")
            robot_index += 1

    def display_winners(self):
        print("The battle has been won!")
        if len(self.fleet.robots) > 0:
            print("robots win!")
        else:
            print("Dinosaurs win!")
