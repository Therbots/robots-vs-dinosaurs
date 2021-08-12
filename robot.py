#CLASS: ROBOT
#AUTHOR: TAYLOR
#DATE: 10AUG21


from weapons import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon('Beam Sword', 50)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power


