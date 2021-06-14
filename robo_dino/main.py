from battlefield import Battlefield
from herd import Dinosaur
from fleet import Robot


if __name__ == '__main__':


    battlefield = Battlefield()
    battlefield.battlefield_welcome()


dinosaur_one = Dinosaur("Sharptooth", 100, 10, 10)
dinosaur_two = Dinosaur("Sara", 100, 10, 10)
dinosaur_three = Dinosaur("Barny", 100, 10, 10)

robot_one = Robot("Walle", 100, 10, 10)
robot_two = Robot("Burnie", 100, 10, 10)
robot_three = Robot("Mo", 100, 10, 10)

