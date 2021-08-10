#CLASS: DINOSAUR
#AUTHOR: TAYLOR
#DATE: 10AUG21



class Dinosaur:
    def __init__ (self, name, attack_power):
        self.name = ''
        self.attack_power = int
        self.health = 100


    def attack (self, robot):
        robot.health -= self.attack_power