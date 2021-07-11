from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.call_the_dinosaurs()

    def call_the_dinosaurs(self):
        sharp_tooth = Dinosaur("Sharptooth", 100, 100, 20)
        sara = Dinosaur("Sara", 100, 100, 15)
        barny = Dinosaur("Barny", 100, 100, 10)
        self.dinosaurs.append(sharp_tooth)
        self.dinosaurs.append(sara)
        self.dinosaurs.append(barny)





