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
        
        
        
    def display_welcome(self):
         print ('Welcome to Robots Vs Dinosaurs battle simulation')

    def battle(self):
        battle_over = False
        while not battle_over:
            self.dino_turn()
            self.robo_turn()
            if self.fleet_1.robot_1.health <= 0 and self.fleet_1.robot_2.health <= 0 and self.fleet_1.robot_3.health <= 0 or self.herd_1.dinosaur_1.health <= 0 and self.herd_1.dinosaur_2.health <= 0 and self.herd_1.dinosaur_3.health <= 0:
                battle_over = True
        self.display_winners()
            
            
        

    def dino_turn(self):
        print("Dino team it's your turn!")
        self.show_dino_opponent_options()


    def robo_turn(self):
        print("Robo team it's your turn!")
        self.show_robo_opponent_options()
       
        

    def show_dino_opponent_options(self):
        user_atk = int(input('To attack with your Velociraptor press "1" for your T-Rex press "2" for your Stegosaurus press "3": '))
        if user_atk == 1:
            if self.herd_1.dinosaur_1.health <= 0:
                print('This dino is deceased! Choose another one!')
                self.dino_turn()
            user_target = int(input('Press "1" to attack Robo Infantry, "2" for Robo Calvary and "3" for Robo Heavy: '))
            if user_target == 1:
                self.herd_1.dinosaur_1.attack(self.fleet_1.robot_1)
                if self.fleet_1.robot_1.health <= 0:
                    print("You destroyed their robot!")
                else:
                    print('Good hit! Their remaining health is ', self.fleet_1.robot_1.health)
            elif user_target == 2:
                self.herd_1.dinosaur_1.attack(self.fleet_1.robot_2)
                if self.fleet_1.robot_2.health <= 0:
                    print("You destroyed their robot!")
                else:
                    print('Good hit! Their remaining health is ', self.fleet_1.robot_2.health)
            elif user_target == 3:
                self.herd_1.dinosaur_1.attack(self.fleet_1.robot_3)
                if self.fleet_1.robot_3.health <= 0:
                    print("You destroyed their robot!")
                else:
                    print('Good hit! Their remaining health is ', self.fleet_1.robot_3.health)
            elif user_atk == 2:
                if self.herd_1.dinosaur_2.health <= 0:
                    print('This dino is deceased! Choose another one!')
                    self.dino_turn()                
                user_target = int(input('Press "1" to attack Robo Infantry, "2" for Robo Calvary and "3" for Robo Heavy: '))
                if user_target == 1:
                    self.herd_1.dinosaur_2.attack(self.fleet_1.robot_1)
                    if self.fleet_1.robot_1.health <= 0:
                        print("You destroyed their robot!")
                    else:
                        print('Good hit! Their remaining health is ', self.fleet_1.robot_1.health)
                elif user_target == 2:
                    self.herd_1.dinosaur_2.attack(self.fleet_1.robot_2)
                    if self.fleet_1.robot_2.health <= 0:
                        print("You destroyed their robot!")
                    else:
                        print('Good hit! Their remaining health is ', self.fleet_1.robot_2.health)
                elif user_target == 3:
                    self.herd_1.dinosaur_2.attack(self.fleet_1.robot_3)
                    if self.fleet_1.robot_3.health <= 0:
                        print("You destroyed their robot!")
                    else:
                        print('Good hit! Their remaining health is ', self.fleet_1.robot_3.health)
            elif user_atk == 3:
                if self.herd_1.dinosaur_1.health <= 0:
                    print('This dino is deceased! Choose another one!')
                    self.dino_turn()
                user_target = int(input('Press "1" to attack Robo Infantry, "2" for Robo Calvary and "3" for Robo Heavy: '))
                if user_target == 1:
                    self.herd_1.dinosaur_3.attack(self.fleet_1.robot_1)
                    if self.fleet_1.robot_1.health <= 0:
                        print("You destroyed their robot!")
                    else:
                        print('Good hit! Their remaining health is ', self.fleet_1.robot_1.health)
                elif user_target == 2:
                    self.herd_1.dinosaur_3.attack(self.fleet_1.robot_2)
                    if self.fleet_1.robot_2.health <= 0:
                        print("You destroyed their robot!")
                    else:
                        print('Good hit! Their remaining health is ', self.fleet_1.robot_2.health)
                elif user_target == 3:
                    self.herd_1.dinosaur_3.attack(self.fleet_1.robot_3)
                    if self.fleet_1.robot_3.health <= 0:
                        print("You destroyed their robot!")
                    else:
                        print('Good hit! Their remaining health is ', self.fleet_1.robot_3.health)
    
        

    def show_robo_opponent_options(self):
        user_atk = int(input('To attack with your Robo Infantry press "1" for your Robo Calvary press "2" for your Robo Heavy press "3": '))
        if user_atk == 1:
            if self.fleet_1.robot_1.health <=0:
                print('This robot has been destroyed! Choose another one!')
                self.robo_turn()
            user_target = int(input('Press "1" to attack Velociraptor, "2" for T-Rex and "3" for Stegosaurus: '))
            if user_target == 1:
                self.fleet_1.robot_1.attack(self.herd_1.dinosaur_1)
                if self.herd_1.dinosaur_1.health <= 0:
                    print("You killed their Dino!")
                else:
                    print('Good hit! Their remaining health is ', self.herd_1.dinosaur_1.health)
            elif user_target == 2:
                self.fleet_1.robot_2.attack(self.herd_1.dinosaur_2)
                if self.herd_1.dinosaur_2.health <= 0:
                    print("You killed their Dino!")
                else:
                    print('Good hit! Their remaining health is ', self.herd_1.dinosaur_2.health)
            elif user_target == 3:
                self.fleet_1.robot_3.attack(self.herd_1.dinosaur_3)
                if self.herd_1.dinosaur_3.health <= 0:
                    print("You killed their Dino!")
                else:
                    print('Good hit! Their remaining health is ', self.herd_1.dinosaur_3.health)
            elif user_atk == 2:
                if self.fleet_1.robot_2.health <=0:
                    print('This robot has been destroyed! Choose another one!')
                    self.robo_turn()
                user_target = int(input('Press "1" to attack Velociraptor, "2" for T-Rex and "3" for Stegosaurus: '))
                if user_target == 1:
                    self.fleet_1.robot_1.attack(self.herd_1.dinosaur_1)
                    print('Their health is at ', self.herd_1.dinosaur_1.health)
                    if self.herd_1.dinosaur_1.health <= 0:
                        print("You killed their Dino!")
                    else:
                        print('Good hit! Their remaining health is ', self.herd_1.dinosaur_1.health)
                elif user_target == 2:
                    self.fleet_1.robot_2.attack(self.herd_1.dinosaur_2)
                    if self.herd_1.dinosaur_2.health <= 0:
                        print("You killed their Dino!")
                    else:
                        print('Good hit! Their remaining health is ', self.herd_1.dinosaur_2.health)
                elif user_target == 3:
                    self.fleet_1.robot_3.attack(self.herd_1.dinosaur_3)
                    if self.herd_1.dinosaur_3.health <= 0:
                        print("You killed their Dino!")
                    else:
                        print('Good hit! Their remaining health is ', self.herd_1.dinosaur_3.health)
            elif user_atk == 3:
                if self.fleet_1.robot_3.health <=0:
                    print('This robot has been destroyed! Choose another one!')
                    self.robo_turn()
                user_target = int(input('Press "1" to attack Velociraptor, "2" for T-Rex and "3" for Stegosaurus: '))
                if user_target == 1:
                    self.fleet_1.robot_1.attack(self.herd_1.dinosaur_1)
                    if self.herd_1.dinosaur_1.health <= 0:
                        print("You killed their Dino!")
                    else:
                        print('Good hit! Their remaining health is ', self.herd_1.dinosaur_1.health)
                elif user_target == 2:
                    self.fleet_1.robot_2.attack(self.herd_1.dinosaur_2)
                    if self.herd_1.dinosaur_2.health <= 0:
                        print("You killed their Dino!")
                    else:
                        print('Good hit! Their remaining health is ', self.herd_1.dinosaur_2.health)
                elif user_target == 3:
                    self.fleet_1.robot_3.attack(self.herd_1.dinosaur_3)
                    if self.herd_1.dinosaur_3.health <= 0:
                        print("You killed their Dino!")
                    else:
                        print('Good hit! Their remaining health is ', self.herd_1.dinosaur_3.health)
 

    def display_winners(self):
        if  self.fleet_1.robot_1.health <= 0 and self.fleet_1.robot_2.health <= 0 and self.fleet_1.robot_3.health <= 0:
            print('Dinosaurs win!')
        elif  self.herd_1.dinosaur_1.health <= 0 and self.herd_1.dinosaur_2.health <= 0 and self.herd_1.dinosaur_3.health <= 0:
            print('Robots win!')