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

super_power = ['Thunder', 'High Voltage', 'Hydro Pump', 'Fire Blast', 'Lava Soup', 'Super Bud', 'Outrage', 'Poison Jab', 'Leaf Hug', '220 Power', 'Sea Power', 'Fire Fly']
normal_power = ['Thunderbolt', 'Surf', 'Bubble Beam', 'Acid', 'Flamethower', 'Fire Spin', 'Vine Whip', 'Thunder Punch', 'Hyper Warm', 'Scald', 'Take Down', 'Bite']
small_power = ['Thunder Shock', 'Scratch', 'Water Gun']

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
        global opponent, player
        #Note: 'opp' must be an object of Pokemon() class 
        if self.defence >= dam:    #If pokemon's def. absorbs all damage
            dam = self.defence + 2
        if opp.type == 'W' and self.type == 'E':    #Types bonuses and effects
            if opp.lives - ((dam - opp.defence) * 2)  >= 0:
                opp.lives -= ((dam - opp.defence) * 2) #Opponent type water, electric power is effective -> x2 damage
        elif opp.type == 'G' and self.type == 'F':
            if opp.lives - ((dam - opp.defence) * 2) >= 0:
                opp.lives -= ((dam - opp.defence) * 2)
        elif opp.type == 'G' and self.type == 'E':
            if opp.lives - ((dam - opp.defence) // 2) >= 0:
                opp.lives -= ((dam - opp.defence) // 2)
        else:
            if opp.lives - (dam - opp.defence) >= 0:    
                opp.lives -= (dam - opp.defence)

    
player = Pokemon('Pokemon 1', 'B', 100, 5)
opponent = Pokemon('Pokemon 2', 'B', 100, 5)
def choose_pokemon():
    global player
    choose = easygui.choicebox('Choose a Pokemon', 'Pokemon Battles', pokemons)
    if choose == 'Bulbasaur' or choose == 'Vileplume':
        type_p = 'G'
    elif choose == 'Squirtle':
        type_p = 'W'
    elif choose == 'Charmonder':
        type_p = 'F'
    else:
        type_p = 'B'
    player = Pokemon(choose, type_p, 100, random.randint(1, 15))

def battle():
    global player, opponent, free
    choose_pokemon()
    easygui.msgbox(f'Your Pokemon will be {player.name}.')
    opp = random.choice(pokemons)
    if opp == 'Bulbasaur' or opp == 'Vileplume':
        type_p = 'G'
    elif opp == 'Squirtle':
        type_p = 'W'
    elif opp == 'Charmonder':
        type_p = 'F'
    elif opp == 'Pikachu':
        type_p = 'E'
    else:
        type_p = 'B'
    opponent = Pokemon(opp, type_p, 100, random.randint(1, 15))
    easygui.msgbox(f"Your opponent's pokemon will be {opponent.name}.")
    free = False


def color_set(type: str):
    global color
    if type == 'G':
        color = 'green'
    elif type == 'W':
        color = 'cyan'
    elif type == 'F':
        color = "#43A52B"
    elif type == 'E':
        color = "#A6FF00"
    else:
        color = "#798885"

def choose_attack(text: str):
    global attk
    attk = text
free = True
sw = 'my'
information = f"{player.name}:{player.lives}hp | {opponent.name}:{opponent.lives}hp"
info = tk.Label(root, text=information)
info.pack()
color = 'grey'
attk = ''
attkk = ''

btn_widgets = []
for i in range(4):
    btn = tk.Button(root, width=20)
    btn.pack(pady=5, padx=10, fill="x")
    btn_widgets.append(btn)

def on_click(attack_name):
    # player switch
    global sw, attk
    attk = attack_name

def update_button_ui():
    # updating the buttons look
    color_set(player.type)
    for i in range(4):
        attack_name = player.attacks[i]
        btn_widgets[i].config(
            text=attack_name,
            bg=color,
            fg="white",

            command=lambda name=attack_name: on_click(name)
        )

def update():
    global free, sw, player, opponent, small_power, super_power, normal_power, basic, elecric, fire, grass, water, info, information, color, attk, attkk
    if free == True:
        battle()
        update_button_ui()
    
    if sw == 'my':
        color_set(player.type)
        buttons = [
            (f"{player.attacks[0]}", color, "white"),
            (f"{player.attacks[1]}", color, "white"),
            (f"{player.attacks[2]}", color, "white"),
            (f"{player.attacks[3]}", color, "white")
        ]

        for i in range(4):
            attack_text = player.attacks[i]
            btn_widgets[i].config(
                text=attack_text,
                bg=color,
                # Используем lambda, чтобы атака срабатывала только при нажатии
                command=lambda t=attack_text: choose_attack(t)
            )
            
            btn.pack(pady=5, padx=10, fill="x")


        if attk in super_power:
            player.hit(opponent, random.randint(30, 55))
            print(opponent.lives)
        else:
            player.hit(opponent, random.randint(10, 25))
            print(opponent.lives)

        easygui.msgbox(F'Your {player.name} used {attk}!')

        sw = 'opp'
    elif sw == 'opp':
        attkk = random.choice(opponent.attacks)
        if attkk in super_power:
            opponent.hit(player, random.randint(30, 55))
            print(player.lives)
        elif attkk == 'Growth':
            opponent.defence += random.randint(1, 8)
        elif attkk == 'Mega Drain':
            player.decrease_lives(25, 'G')
            opponent.heal_lives(25)
        else:
            opponent.hit(player, random.randint(10, 25))
            print(player.lives)


        easygui.msgbox(F"Your opponent's {opponent.name} used {attk}!")
        sw = 'my'

        
    information = f"{player.name}:{player.lives}hp | {opponent.name}:{opponent.lives}hp"
    info.config(text=information)

    if player.lives <= 0 or opponent.lives <= 0:
        if player.lives <= 0:
            easygui.msgbox(f"You can't battle! {opponent.name} is winner!")
            quit()
        else:
            easygui.msgbox(f"You win this battle! {player.name} is winner!")
            quit()

    root.after(100, update)

root.after(100, update)
root.mainloop()
