#CLASS: BATTLEFIELD
#AUTHOR: TAYLOR
#DATE: 10AUG21

from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.herd_1 = Herd()
        self.fleet_1 = Fleet()
        

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
        
        
    def display_welcome(self):
         print ('Welcome to Robots Vs Dinosaurs battle simulation')

    def battle(self):
        self.dino_turn()
        self.robo_turn()
        

    def dino_turn(self):
       self.show_dino_opponent_options()


    def robo_turn(self):
        self.show_robo_opponent_options()
       
        

    def show_dino_opponent_options(self):
        user_turn_choice =  int(input('Press "1" to attack and "2" to pass: '))
        if user_turn_choice == 1:
            user_atk = int(input('To attack with your Velociraptor press "1" for your T-Rex press "2" for your Stegosaurus press "3": '))
            if user_atk == 1:
                if self.herd_1.dinosaur_1.health == 0:
                    print('That Dino is dead!')
                user_target = int(input('Press "1" to attack Robo Infantry, "2" for Robo Calvary and "3" for Robo Heavy: '))
                if user_target == 1:
                    self.herd_1.dinosaur_1.attack(self.fleet_1.robot_1)
                elif user_target == 2:
                    self.herd_1.dinosaur_1.attack(self.fleet_1.robot_2)
                elif user_target == 3:
                    self.herd_1.dinosaur_1.attack(self.fleet_1.robot_3)
            elif user_atk == 2:
                user_target = int(input('Press "1" to attack Robo Infantry, "2" for Robo Calvary and "3" for Robo Heavy: '))
                if user_target == 1:
                    self.herd_1.dinosaur_2.attack(self.fleet_1.robot_1)
                elif user_target == 2:
                    self.herd_1.dinosaur_2.attack(self.fleet_1.robot_2)
                elif user_target == 3:
                    self.herd_1.dinosaur_2.attack(self.fleet_1.robot_3)
            elif user_atk == 3:
                 user_target = int(input('Press "1" to attack Robo Infantry, "2" for Robo Calvary and "3" for Robo Heavy: '))
                 if user_target == 1:
                    self.herd_1.dinosaur_3.attack(self.fleet_1.robot_1)
                 elif user_target == 2:
                    self.herd_1.dinosaur_3.attack(self.fleet_1.robot_2)
                 elif user_target == 3:
                    self.herd_1.dinosaur_3.attack(self.fleet_1.robot_3)
        elif user_turn_choice == 2:  
            pass       
        

    def show_robo_opponent_options(self):
        user_turn_choice =  int(input('Press "1" to attack and "2" to pass: '))
        if user_turn_choice == 1:
            user_atk = int(input('To attack with your Robo Infantry press "1" for your Robo Calvary press "2" for your Robo Heavy press "3": '))
            if user_atk == 1:
                user_target = int(input('Press "1" to attack Velociraptor, "2" for T-Rex and "3" for Stegosaurus: '))
                if user_target == 1:
                    self.fleet_1.robot_1.attack(self.herd_1.dinosaur_1)
                elif user_target == 2:
                    self.fleet_1.robot_2.attack(self.herd_1.dinosaur_2)
                elif user_target == 3:
                    self.fleet_1.robot_3.attack(self.herd_1.dinosaur_3)
            elif user_atk == 2:
                user_target = int(input('Press "1" to attack Velociraptor, "2" for T-Rex and "3" for Stegosaurus: '))
                if user_target == 1:
                    self.fleet_1.robot_1.attack(self.herd_1.dinosaur_1)
                elif user_target == 2:
                    self.fleet_1.robot_2.attack(self.herd_1.dinosaur_2)
                elif user_target == 3:
                    self.fleet_1.robot_3.attack(self.herd_1.dinosaur_3)
            elif user_atk == 3:
                 user_target = int(input('Press "1" to attack Velociraptor, "2" for T-Rex and "3" for Stegosaurus: '))
                 if user_target == 1:
                    self.fleet_1.robot_1.attack(self.herd_1.dinosaur_1)
                 elif user_target == 2:
                    self.fleet_1.robot_2.attack(self.herd_1.dinosaur_2)
                 elif user_target == 3:
                    self.fleet_1.robot_3.attack(self.herd_1.dinosaur_3)
        elif user_turn_choice == 2:  
            pass       

    def display_winners(self):
        if self.fleet_1 == 0:
            print('Dinosaurs win!')
        else:
            print('Robots win!')