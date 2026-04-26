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
basic = ['Scratch', 'Bite', 'Poison Sting', 'Poison Jab', 'Quick Attack', 'Take Down', 'Outrage', 'Smart']

super_power = ['Thunder', 'High Voltage', 'Hydro Pump', 'Fire Blast', 'Lava Soup', 'Outrage', 'Poison Jab', 'Leaf Hug', '220 Power', 'Fire Fly']
normal_power = ['Thunderbolt', 'Surf', 'Bubble Beam', 'Acid', 'Flamethower', 'Fire Spin', 'Vine Whip', 'Thunder Punch', 'Hyper Warm', 'Scald', 'Take Down', 'Bite']
small_power = ['Thunder Shock', 'Scratch', 'Water Gun']

special = ['Super Bud', 'Mega Drain', 'Growth', 'Sea Power', 'Smart']

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
                self.lives -= ((dam - self.defence) * 2)
        elif opp_type == 'F' and self.type == 'G':
            if self.lives - ((dam - self.defence) * 2) >= 0:
                self.lives -= ((dam - self.defence) * 2)
        elif opp_type == 'E' and self.type == 'G':
            if self.lives - ((dam - self.defence) // 2) >= 0:
                self.lives -= ((dam - self.defence) // 2)
        else:
            if self.lives - (dam - self.defence) >= 0:    #All diffrent types - normal damage
                self.lives -= (dam - self.defence)
        
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

free = True
sw = 'my'
information = f"{player.name}:{player.lives}hp | {opponent.name}:{opponent.lives}hp"
info = tk.Label(root, text=information)
info.pack()
color = 'grey'
player_attack = ''
max_attacks = 4
can_switch = True

btn_widgets = []
for i in range(4):
    btn = tk.Button(root, width=20)
    btn.pack(pady=5, padx=10, fill="x")
    btn_widgets.append(btn)

def locked():
    global btn_widgets
    for i in btn_widgets:
        i.config(
            state = 'disabled',
        )

def unlocked():
    global btn_widgets
    for i in btn_widgets:
        i.config(
            state = 'active',
        )
    

def attack(name):
    global player_attack
    player_attack = name
    update_button_ui()
    locked()

    root.after(1000, perform_opponent_move)

def update_button_ui():
    global max_attacks
    # updating the buttons look
    color_set(player.type)
    for i in range(max_attacks):
        attack_name = player.attacks[i]
        btn_widgets[i].config(
            text=attack_name,
            bg=color,
            fg="black",
            command=lambda: attack(attack_name)
        )

def player_turn():
    global can_switch
    can_switch = False
    if player_attack in super_power:
        player.hit(opponent, random.randint(31, 55))
    elif player_attack in normal_power:
        player.hit(opponent, random.randint(20, 30))
    elif player_attack in small_power:
        player.hit(opponent, random.randint(10, 19))
    elif player_attack in special:
        if player_attack == 'Mega Drain':
            drain = random.randint(25, 40)
            player.hit(opponent, drain)
            player.heal_lives(drain)
        elif player_attack == 'Growth':
            player.defence += random.randint(1, 8)
        elif player_attack == 'Super Bud':
            player.defence += random.randint(1, 12)
            if (random.randint(1, 100)) < 20:
                player.heal_lives(20)
        elif player_attack == 'Sea Power':
            player.defence += random.randint(1, 12)
            if (random.randint(1, 100)) < 20:
                player.heal_lives(20)
        elif player_attack == 'Smart':
            player.attacks = []
            player.attacks = random.sample(basic, 4)
            player.heal_lives(5)
            player.defence += 2
    can_switch = True
    


        

def opponent_turn():
    global can_switch
    locked()
    if can_switch:
        opp_attack = random.choice(opponent.attacks)
        if opp_attack in super_power:
            opponent.hit(player, random.randint(31, 55))
        elif opp_attack in normal_power:
            opponent.hit(player, random.randint(20, 30))
        elif opp_attack in small_power:
            opponent.hit(player, random.randint(10, 19))
        elif opp_attack in special:
            if opp_attack == 'Mega Drain':
                drain = random.randint(25, 40)
                opponent.hit(player, drain)
                opponent.heal_lives(drain)
            elif opp_attack == 'Growth':
                opponent.defence += random.randint(1, 8)
            elif opp_attack == 'Super Bud':
                opponent.defence += random.randint(1, 12)
                if (random.randint(1, 100)) < 20:
                    opponent.heal_lives(20)
            elif opp_attack == 'Sea Power':
                opponent.defence += random.randint(1, 12)
                if (random.randint(1, 100)) < 20:
                    opponent.heal_lives(20)
            elif opp_attack == 'Smart':
                opponent.attacks = []
                opponent.attacks = random.sample(basic, 4)
                opponent.heal_lives(5)
                opponent.defence += 2

        easygui.msgbox(f"Your opponent's {opponent.name} used {opp_attack}!")
        can_switch = False

def perform_opponent_move():
    opponent_turn()
    update_button_ui() # Обновляем HP после удара компьютера
    unlocked()       # Возвращаем кнопки игроку

def update():
    global free, sw, player, opponent, small_power, super_power, normal_power, basic, elecric, fire, grass, water, info, information, color
    if free == True:
        battle()
        update_button_ui()
    
    player_turn()
    opponent_turn()
        
    information = f"{player.name}:{player.lives}hp | {opponent.name}:{opponent.lives}hp"
    info.config(text=information)

    if player.lives <= 0 or opponent.lives <= 0:
        if player.lives <= 0:
            easygui.msgbox(f"You can't battle! {opponent.name} is winner!")
            quit()
        else:
            easygui.msgbox(f"You win this battle! {player.name} is winner!")
            quit()

    root.after(1000, update)

root.after(1000, update)
root.mainloop()