import pygame
import random
import easygui
import tkinter as tk
root = tk.Tk()
pygame.mixer.init()
main_music = pygame.mixer.music.load('Trainer_Battle.mp3')
pokemons = ['Pikachu', 'Vileplume', 'Charmonder', 'Squirtle', 'Iyisaur', 'Rattata']
grass = ['Mega Drain', 'Leaf Hug', 'Growth', 'Vine Whip', 'Super Bud', 'Poison Powder', 'Poison Jab', 'Poison Sting', 'Acid']
water = ['Water Gun', 'Surf', 'Bubble Beam', 'Hydro Pump', 'Scald', 'Sea Power', 'Wave', 'Hydro']
elecric = ['Thunder Shock', 'Thunder', 'Thunderbolt', 'High Voltage', '220 Power', 'Thunder Punch']
fire = ['Fire Blast', 'Flamethower', 'Fire Spin', 'Lava Soup', 'Earthflame', 'Fire Fly', 'Hyper Warm']


root.mainloop()
