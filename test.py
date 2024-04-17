import random
import time

class hero():
    name = input("Please name your hero: ")
    health = 30
    defense = 10
    strength = 15
    atk = 20

class goblin():
    name = "Goblin"
    health = 15
    defense = 10
    strength = 8
    atk = 15

def hero_attack():
    atk = hero.atk
    strength = hero.strength
    hero_hp = hero.health
    atk_roll = random.randint(0,atk)
    str_roll = random.randint(0,strength)

    gob_atk = goblin.atk
    gob_strength = goblin.strength
    gob_hp = goblin.health
    gob_atk_roll = random.randint(0,gob_atk)
    gob_str_roll = random.randint(0,gob_strength)
#Hero attack
    while (hero_hp > 0 or gob_hp > 0):
        print("You roll a " + str(atk_roll))
        enemy_def = goblin.defense
        if (atk_roll >= goblin.defense):
            print ("You have hit the " + goblin.name)
            time.sleep(0.5)
            gob_hp = (gob_hp - str_roll)
            print ("You have dealt " + str(str_roll) + " damage.")
            time.sleep(0.5)
            if (gob_hp <= 0):
                print("The goblin has been defeated!")
                break
            else:    
                print ("The " + goblin.name + " now has " + str(gob_hp) + " HP left")
        else:
            print ("You have missed the " + goblin.name)
#Goblin attack
        print("The Goblin rolls a " + str(gob_atk_roll))
        hero_def = hero.defense
        if (gob_atk_roll >= hero.defense):
            print ("The Goblin has hit you")
            time.sleep(0.5)
            hero_hp = (hero_hp - gob_str_roll)
            print("The Goblin has dealt " + str(gob_str_roll) + " damage.")
            time.sleep(0.5)
            if (hero_hp <= 0):
                print("You have died!")
                break
            else:    
                print ("You now have " + str(hero_hp) + " HP left")
        else:
            print ("The Goblin has missed you")
#Defunct. Need to delete once integrated into hero_attack()
"""def goblin_attack():
    atk = goblin.atk
    atk_roll = random.randint(0,atk)
    print("The Goblin rolls a " + str(atk_roll))
    hero_def = hero.defense
    if (atk_roll >= hero.defense):
        print ("The Goblin has hit you")
    else:
        print ("The Goblin has missed you")"""


print("Welcome, " + hero.name + ", to the RNG RPG!")

while True:
    option = input ("""Please select an option:
       1. Fight
       2. Trade
       3. Exit
       Option: \n""")

    if (option == "1"):
        print ("Fighting...")
        hero_attack()
        #goblin_attack()


