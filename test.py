input("IS NOT GAME!!!")
import os
from main import *
os.system("cls")
player = make_hero(name="Вася Питонов", inventory=["зелье"], hp_now=100)

game = True
while game:
    visit_hub(player)

