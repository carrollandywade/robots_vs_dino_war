from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaur = []
        self.call_the_dinosaurs()

    def call_the_dinosaurs(self):
        sharp_tooth = Dinosaur("Sharptooth", 100, 10, 10)
        sara = Dinosaur("Sara", 100, 10, 10)
        barny = Dinosaur("Barny", 100, 10, 10)
        self.dinosaur.append(sharp_tooth)
        self.dinosaur.append(sara)
        self.dinosaur.append(barny)


