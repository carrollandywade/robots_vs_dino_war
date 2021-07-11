from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.assemble_fleet()

    def assemble_fleet(self):
        walle = Robot("Walle", 100, 100)
        burnie = Robot("Burnie", 100, 100)
        mo = Robot("Mo", 100, 100)
        self.robots.append(walle)
        self.robots.append(burnie)
        self.robots.append(mo)








