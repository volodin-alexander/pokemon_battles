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
    def __init__(self, name: str, type: str, lives: int | float):
        self.name = name
        self.type = type
        self.lives = lives
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



root.mainloop()
