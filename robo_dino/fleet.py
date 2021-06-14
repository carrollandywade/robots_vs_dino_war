from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.assemble_fleet()


    def assemble_fleet(self):
        walle = Robot("Walle", 100, 10, 10)
        burnie = Robot("Burnie", 100, 10, 10)
        mo = Robot("Mo", 100, 10, 10)
        self.robots.append(walle)
        self.robots.append(burnie)
        self.robots.append(mo)








