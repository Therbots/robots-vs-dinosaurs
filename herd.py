#CLASS: HERD
#AUTHOR: TAYLOR
#DATE: 10AUG21

from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.herd = []
        self.dinosaur_1 = Dinosaur('Velociraptor', 10, 100)
        self.dinosaur_2 = Dinosaur('T-Rex', 20, 150)
        self.dinosaur_3 = Dinosaur('Stegosaurus', 15, 200)

    def create_herd(self):
        self.herd.append(self.dinosaur)
       


