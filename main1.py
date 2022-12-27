import os
from random import randint, choice

first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый")


def make_hero(
        name=None,
        hp_now=None,
        hp_max=None,
        lvl=1,
        xp_now=0,
        weapon=None,
        sheald=None,
        attack=1,
        defence=1,
        luck=1,
        money=None,
        inventory=None,
) -> dict:
    if not name:
        name = choice(first_names) + " " + choice(last_names)

    if not hp_now:
        hp_now = randint(1, 100)
    
    if not hp_max:
        hp_max = hp_now

    xp_next = lvl * 100

    if money is None:
        money = randint(0, 100)

    if not inventory:
        inventory = []

    if not weapon:
        weapon = {
            "тип": "оружие",
            "название": "Обычный меч",
            "стат": 'атака',
            "модификатор": 2,
            "цена": 10,
        }
    return {
        "имя": name,
        "здоровье": hp_now,
        "здоровье макс": hp_max,
        "уровень": lvl,
        "опыт": xp_now,
        "опыта осталось": xp_next,
        "оружие": weapon,
        "атака": attack,
        "защита": defence,
        "оружие": weapon,
        "щит": sheald,
        "удача": luck,
        "деньги": money,
        "инвентарь": inventory
    }

def equip_item(hero: dict):
    '''
    показать пронумерованные предметы 
        только щиты и оружия? 
        или все предметы?

    выбирается предмет:
        если другой предмет юыл экипирован:
            положить предмет в инвентарь
            статы предмета добавляются к статам персонажа
            оружие персонажа становится выбранным предметом
            этот предмет исчезает из инвентаря 
        
        если никакого предмета не юыло жкипированно:
            статы предмета добавляются к статам персонажа
            оружие персонажа становится выбранным предметом
            этот предмет исчезает из инвентаря 
    пересчитать статы
    '''
    pass


def show_item(item: dict) -> None:
    if item is None:
        print("-нет-")
    else:
        if item['модификатор'] >= 0:
            print(f"{item['название']} + {item['модификатор']} {item['стат']}")
        else:
            print(f"{item['название']} {item['модификатор']} {item['стат']}")


def show_equipped(hero: dict) -> None:
    print("оружие", end=' ')
    show_item(hero['оружие'])
    print("щит", end=' ')
    show_item(hero['щит'])


def show_items(items: list) -> None:
    print("предметы:")
    for num, item in enumerate(items):
        print(f"{num}.", end=" ")
        show_item(item)
    else:
        print("-это конец списка-")

def show_hero(hero:dict) -> None:
    print("имя:", hero['имя'])
    print("здоровье:", hero['здоровье'], "/", hero['здоровье макс'])
    print("уровень:", hero['уровень'])
    print("опыт:", hero['опыт'], "/", hero['опыта осталось'])
    show_equipped(hero)
    print("атака:", hero['атака'])
    print("защита:", hero['защита'])
    print("удача:", hero['удача'])
    print("деньги:", hero['деньги'])
    show_items(hero['инвентарь'])
    print("")


def levelup(hero: dict) -> None:
    """
    TODO: что растет с уровнем?
    """
    while hero['опыт'] >= hero['опыта осталось']:
        hero['уровень'] += 1
        hero['опыта осталось'] = hero['уровень'] * 100
        print(f"{hero['имя']} получил {hero['уровень']} уровень\n")


def buy_item(hero: dict, price: int, item: str) -> None:
    """
    Удаляет предмет из инвентаря по индексу и дает герою эффект этого предмета
    """
    if idx <= len(hero['инвентарь']) - 1 and idx > -1:
        print(f"{hero['имя']} употребил {hero['инвентарь'][idx]}")
        if hero['инвентарь'][idx] == "зелье":
            hero['здоровье'] += 10
            if hero['здоровье'] > hero['здоровье макс']:
                hero['здоровье'] = hero['здоровье макс']
        elif hero['инвентарь'][idx] == "яблоко":
            pass
        else:
            print("Никакого эффекта")
        hero['инвентарь'].pop(idx)
    else:
        print("Нет такого индекса!")
    print("")


def consume_item(hero: dict) -> None:
    """
    Ставка от 1 монеты до количества монет героя
    Игрок и казино бросаю кости, кто больше, то забирает ставку
    TODO: Как удача влияет на кости?
    """
    try:
        bet = int(bet)
    except ValueError:
        print("Ставка недопустима")
    else:
        if bet > 0:
            if hero['деньги'] >= bet:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"{hero['имя']} выбросил {hero_score}")
                print(f"Трактирщик выбросил {casino_score}")
                if hero_score > casino_score:
                    hero['деньги'] += bet
                    print(f"{hero['имя']} выиграл {bet} монет")
                elif hero_score < casino_score:
                    hero['деньги'] -= bet
                    print(f"{hero['имя']} проиграл {bet} монет")
                else:
                    print("Ничья!")
            else:
                print(f"У {hero['имя']} нет денег на такую ставку!")
        else:
            print("Ставки начинаются от 1 монеты!")


def play_dice(hero: dict, bet: str) -> None:
    """
    Ставка от 1 монеты до количества монет героя
    Игрок и казино бросаю кости, кто больше, то забирает ставку
    TODO: Как удача влияет на кости?
    """
    try:
        bet = int(bet)
    except ValueError:
        print("Ставка должна быть числом!")
    else:
        if bet > 0:
            if hero['деньги'] >= bet:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"{hero['имя']} выбросил {hero_score}")
                print(f"Трактирщик выбросил {casino_score}")
                if hero_score > casino_score:
                    hero['деньги'] += bet
                    print(f"{hero['имя']} выиграл {bet} монет")
                elif hero_score < casino_score:
                    hero['деньги'] -= bet
                    print(f"{hero['имя']} проиграл {bet} монет")
                else:
                    print("Ничья!")
            else:
                print(f"У {hero['имя']} нет денег на такую ставку!")
        print("Ставки начинаются от 1 монеты")
    input("\nНажмите ENTER чтобы продолжить")



def combat_turn(attacker, defender):
   if attacker['здоровье'] > 0:
        damage = attacker['атака']
        defender['здоровье'] -= damage
        print(f"{attacker['имя']} ударил {defender['имя']} на {damage} жизней!")
    


def start_fight(hero: dict) -> None:
    os.system("cls")
    """
    Зависит ли враг от уровня героя?
    Формула аткаи и защиты?
    Можно ли выпить зелье в бою?
    """
    enemy = make_hero(hp_now=30, xp_now=123, inventory=["вражеский меч", "вражеский конь"])
    text = ""
    while hero['здоровье'] > 0 and enemy['здоровье'] > 0:
        show_hero(hero)
        show_hero(enemy)
        options = [
            "атаковать",
            "применить предмет из инвентаря",
        ]
        show_option(hero, options)
        option = choose_option(hero, options)
        os.system("cls")
        if option == 0:
            combat_turn(hero, enemy)
            combat_turn(enemy, hero)
        print("")
    count_fight_result(hero, enemy)



def count_fight_result(hero, enemy):
    if hero['здоровье'] > 0 and enemy['здоровье'] <= 0:
        print(f"{hero['имя']} победил и получает в награду:")
        hero['опыт'] += enemy['опыт']
        print(enemy['опыт'], "опыта")
        hero['деньги'] += enemy['деньги']
        print(enemy['деньги'], "монет")
        print("и предметы: ", end="")
        for item in enemy['инвентарь']:
            print(item, end=", ")
        hero['инвентарь'] += enemy['инвентарь']
        levelup(hero)
    elif hero['здоровье'] <= 0 and enemy['здоровье'] > 0:
        print(f"{enemy['имя']} победил!")
        print("Игра должна закончиться тут!")
    else:
        print(f"{hero['имя']} и {enemy['имя']} пали в бою:(")
        print("Игра должна закончиться тут!")
    input("\nНажмите ENTER чтобы продолжить")
    

def choose_option(hero: dict, options: dict) -> int:
    """
    Получает ввод пользователя
    Проверяет ввод и возвращает его, если он есть в вариантах
    """
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:  # выполнится, если try не получится
        print("Ввод должен быть целым неотрицательным числом")
    else:  # выполнится, если try удался
        if option < len(options) and option > -1:
            return option
        else:
            print("Нет такого выбора")


def visit_hub(hero):
    show_hero(hero)
    text = f"{hero['имя']} приехал к Хаб, здесь есть чем заняться:"
    options = [
        "заглянуть в лавку алхимика",
        "пойти в казино",
        "пойти на арену",
        "выйти в главное меню"
    ]
    show_option(hero, options)
    option = choose_option(hero, options)
    os.system("cls")
    if option == 0:
        return visit_shop(hero)
    elif option == 1:
        return visit_casino(hero)
    elif option == 2:
        return visit_arena(hero)
    elif option == 3:
        print("пока! привет!")
    input("\nНажмите ENTER чтобы продолжить")


def visit_shop(hero:dict) -> None:
    show_hero(hero)
    text = f"{hero['имя']} приехал в лавку алхимика. здесь странно пахнет и продаются зелья. "
    options = ["купить зелье лечения за 10 монет",
        "купить зелье опыта ха 30 монет",
        "выйти из лавки в хаб",
        ]
    show_option(hero, options)
    option = choose_option(hero, options)
    if option == 0:
        buy_item(hero, 10, "зелье лечение")
        return visit_shop(hero)
    elif option == 1:
        buy_item(hero, 30, "зелье опыта")
        return visit_shop(hero)
    elif option == 2:
         return visit_hub(hero)
    input("\nНажмите ENTER чтобы продолжить ")


def visit_casino(hero: dict) -> None:
    show_hero(hero)
    text = f"{hero['имя']} приехал в казино. за вами следят охраники. "
    options = ["сесть за ближайший стол",
        "выйти из лавки в хаб",
        ]
    show_option(hero, options)
    option = choose_option(hero, options)
    if option == 0:
        print("вы сели за стол")
        bet = input("Выберите ставку: ")
        return play_dice(hero, bet)
    elif option == 1:
        return visit_hub(hero)
        
    input("\nНажмите ENTER чтобы продолжить ")


def visit_arena(hero: dict) -> None:
    show_hero(hero)
    text = f"{hero['имя']} вы приехалт на арену."
    options = [
        "Сражаться",
        "Съесть предмет из инвентаря",
        "Выйти в Хаб"
    ]
    os.system("cls")
    show_option(hero, options)

    if "зелье лечения" in hero['инвентарь']:
        options.append("Выпить зелье лечения")
    option = choose_option(hero, options)
    if option == 0:
        start_fight(hero)
        return visit_arena(hero)
    elif option == 1:
        idx = choose_option(hero, "", hero['инвентарь'])
        os.system("cls")
        if idx is not None:
            consume_item(hero, idx)
        input("\nНажмите ENTER чтобы продолжить")
        return visit_arena(hero)
    elif option == 2:
        return visit_hub(hero)


def show_option(hero:dict, options:dict):
    for num, option in enumerate(options):
            print(f"{num}. {option}")

   









print("у и что ты ожидал здесь увидеть?")