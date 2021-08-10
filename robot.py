#CLASS: ROBOT
#AUTHOR: TAYLOR
#DATE: 10AUG21


from weapons import Weapon

class Robot:
    def __init__ (self, name):
        self.name = ''
        self.health = 100
        self.weapon = Weapon()

    def attack (self, dinosaur):
        dinosaur.health -= self.weapon.attack_power


weapon = Weapon ('Beam Sword', 15)