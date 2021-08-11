#CLASS: FLEET
#AUTHOR: TAYLOR
#DATE: 10AUG21

from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet = []
        self.robot_1 = Robot('Robo Infantry', 150)
        self.robot_2 = Robot('Robo Calvary', 100)
        self.robot_3 = Robot('Robo Heavy', 200)

    def create_fleet(self):
        self.fleet.append(self.robot_20)

