from main import *

player = make_hero(name="Вася Питонов", inventory=["зелье"], hp_now=100)

game = True
while game:
    visit_hub(player)

