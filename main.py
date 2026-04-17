import pygame
import random
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

def animate_hp(target_hp, hp: int, damage: int):
    global current_hp
    if current_hp > target_hp:
        hp -= damage  
        
        # New HP size
        new_x1 = 50 + (current_hp * 2)
        canvas.coords(hp_rect, 50, 50, new_x1, 80)
        
        # next step of animation after 10 milliseconds
        root.after(10, lambda: animate_hp(target_hp, current_hp, 100))


hp_logic = 100    # HP
current_hp = 100  # state in animation

# rectangle
canvas.create_rectangle(50, 50, 250, 80, fill="grey")
hp_rect = canvas.create_rectangle(50, 50, 250, 80, fill="green")
root.mainloop()
