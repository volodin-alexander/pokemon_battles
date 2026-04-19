import pygame
import random        #Loading modules
import easygui
import tkinter as tk
root = tk.Tk()
pygame.mixer.init()
main_music = pygame.mixer.music.load('Trainer_Battle.mp3')   #Load music
pokemons = ['Pikachu', 'Vileplume', 'Charmonder', 'Squirtle', 'Iyisaur', 'Rattata']   #All pokemons (only basic for simple vesion)
grass = ['Mega Drain', 'Leaf Hug', 'Growth', 'Vine Whip', 'Super Bud', 'Poison Powder', 'Poison Jab', 'Poison Sting', 'Acid']   #Basic attacks list 
water = ['Water Gun', 'Surf', 'Bubble Beam', 'Hydro Pump', 'Scald', 'Sea Power', 'Wave', 'Hydro']
elecric = ['Thunder Shock', 'Thunder', 'Thunderbolt', 'High Voltage', '220 Power', 'Thunder Punch']
fire = ['Fire Blast', 'Flamethower', 'Fire Spin', 'Lava Soup', 'Earthflame', 'Fire Fly', 'Hyper Warm']
basic = ['Scratch', 'Bite', 'Poison Sting', 'Poison Jab', 'Quick Attack', 'Take Down', 'Outrage']

class Pokemon():  #Class of pokemons
    def __init__(self, name: str, type: str, lives: int | float, defence: int):
        self.name = name
        self.type = type
        self.lives = lives
        self.defence = defence
        #G = grass-type
        #W = water-type
        #F = fire-type
        #B - basic type (Rattata)
        #.....

        if self.type == 'G':   #Checking attacks
            #G = grass-type
            self.attacks = random.sample(grass, 4)
        elif self.type == 'W':
            self.attacks = random.sample(water, 4)
        elif self.type == 'F':
            self.attacks = random.sample(fire, 4)
        elif self.type == 'E':
            self.attacks = random.sample(elecric, 4)
        elif self.type == 'B':
            self.attacks = random.sample(basic, 4)
        else:
            self.attacks = random.sample(basic, 4)  #If unknow type - basic type

    def decrease_lives(self, dam: int, opp_type: str):
        if self.defence >= dam:    #If pokemon's def. absorbs all damage
            dam = self.defence + 2
        if opp_type == 'E' and self.type == 'W':    #Types bonuses and effects
            if self.lives - ((dam - self.defence) * 2)  >= 0:
                self.lives - ((dam - self.defence) * 2)
        elif opp_type == 'F' and self.type == 'G':
            if self.lives - ((dam - self.defence) * 2) >= 0:
                self.lives - ((dam - self.defence) * 2)
        elif opp_type == 'E' and self.type == 'G':
            if self.lives - ((dam - self.defence) // 2) >= 0:
                self.lives - ((dam - self.defence) // 2)
        else:
            if self.lives - (dam - self.defence) >= 0:    #All diffrent types - normal damage
                self.lives - (dam - self.defence)
        
    def heal_lives(self, heal: int):   #Heal function / for attack 'Mega Drain'
        if (self.lives + heal) <= 100:
            self.lives += heal
        else:
            self.lives += (100 - self.lives) # example, if you don't know it: lives=80, heal=30 -> 80+30=110, 110 > 100; 80 + (100 - 80 = 20) = 100

    def hit(self, opp, dam: int):
        #Note: 'opp' must be an object of Pokemon() class 
        if self.defence >= dam:    #If pokemon's def. absorbs all damage
            dam = self.defence + 2
        if opp.type == 'W' and self.type == 'E':    #Types bonuses and effects
            if opp.lives - ((dam - opp.defence) * 2)  >= 0:
                opp.lives - ((dam - opp.defence) * 2) #Opponent type water, electric poer is effective -> x2 damage
        elif opp.type == 'F' and self.type == 'G':
            if opp.lives - ((dam - opp.defence) * 2) >= 0:
                opp.lives - ((dam - opp.defence) * 2)
        elif opp.type == 'G' and self.type == 'E':
            if opp.lives - ((dam - opp.defence) // 2) >= 0:
                opp.lives - ((dam - opp.defence) // 2)
        else:
            if opp.lives - (dam - opp.defence) >= 0:    
                opp.lives - (dam - opp.defence)


root.mainloop()
