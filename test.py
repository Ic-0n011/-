from main import *

player = make_hero(name="Вася Питонов", inventory=["зелье лечения"], hp_now=100)

game = True
while game:
    visit_hub(player)


#def shoose_inv(hero: list, text: str, options: list):
#   os.system("cls")
#    for num, option in enumerate(options):
#        print(f"{num}. {options}")
#    option = input("\nВведите номер варианта и нажмите ENTER: ")
#    try:
#        optionv = 
