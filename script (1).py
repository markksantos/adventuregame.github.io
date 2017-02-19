### CODE DAY CHALLENGE by Simon Dziak , Mark and Daniel Santos

import sys
import math
import os
import time
import random

weapons = {"Survivor Sword":40}

global HasComputer
HasComputer = "False"

global BrokeComputer
BrokeComputer = "True"

global hasFlashDrive
hasFlashDrive = "False"

class Player:
    def __init__(self, name):
        self.name = name
#HEALTH
        maxHealth = 100
        self.maxHealth = maxHealth
        self.health = maxHealth
#ATTACK
        maxAttack = 100
        self.base_attack = 10
#LEVELS
        startLevel = 1
        self.level = startLevel
        self.maxLevel = 121
#ACCESSORIES
        self.pot = 1
        self.gold = 0
        self.weap = ["Hand"]
        self.currentWeap = ["Hand"]

        @property
        def attack(self):
                attack = self.base_attack
                if currentWeap == {"Hand"}:
                    attack += 5

                if currentWeap == {"Survivor Sword"}:
                    attack += 10

                return attack


class Skeleton:
    def __init__(self, name):
        self.name = "Skeleton"
#HEALTH
        maxHealth = 50
        self.maxHealth = maxHealth
        self.health = maxHealth
#ATTACK
        self.attack = 5
#PLAYER GAINS
        self.goldgain = 10
SkeletonAI = Skeleton('Skeleton')

class Zombie:
    def __init__(self, name):
        self.name = "Zombie"
#HEALTH
        maxHealth = 70
        self.maxHealth = maxHealth
        self.health = maxHealth
#ATTACK
        self.attack = 7
#PLAYER GAINS
        self.goldgain = 15
ZombieAI = Zombie('Zombie')

def main():
    os.system("clear")
    print("Welcome to the Adventure Game \n ")
    print "1. Start"
    print "2. Load Save"
    print "3. Exit"
    option = int(raw_input("-> "))
    if option == 1:
        start()
    elif option == 2:
        pass
    elif option == 3:
        sys.Exit()
    else:
        main()

def start():
    os.system('clear')
    print "Hello, What is your name?"
    option = raw_input("-> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

def start1():
    os.system('clear')
    print "Welcome to your Adventure, %s! You decide the future... \n" % PlayerIG.name
    print "Loading your current stats:"
    time.sleep(1)
    print "Name: %s" % PlayerIG.name
    print "Level: %i" % PlayerIG.level
    print "Gold: %d" % PlayerIG.gold
    print "Potions: %d" % PlayerIG.pot
    print "Attack: %i" % PlayerIG.base_attack
    # print "Current Weapon: %s" % PlayerIG.currentWeap
    print "Health: %i/100\n" % PlayerIG.health
    print " "
    print "1. Play"
    print "2. Save"
    print "3. Exit"
    option = raw_input("-> ")
    if option == "1":
        begin()
    if option == "2":
        pass
    if option == "3":
        pass
    if option == "4":
        notRescued()
    else:
        start1()

def begin():
    os.system('clear')
    print "PRELOG:"
    time.sleep(2)
    print "After a long, and hard day of coding... you're going to sleep in order to present what you made the next day with excitment!\n"
    time.sleep(5)
    print "CHAPTER 1 - AWAKENING    OBJECTIVE: Get back to the facility before noon."
    time.sleep(4)
    print "... You wake up in a forest, stranded and confused. You don't know what happened, or how you got there. You get up, check your pockets and realize you have nothing.\n"
    time.sleep(4)
    print "1) Where am I?"
    print "2) Where is my stuff?"

    option = int(raw_input("-> "))
    if option == 1:
        oneWalk()
    elif option == 2:
        myStuff()
    elif option == 3:
        pass
    else:
        start1()

# Where is my stuff?
def myStuff():
    hasComputer = "False"
    BrokeComputer = "False"
    os.system('clear')
    print "You get up and wonder what to do next..."
    print "1. Check Pockets"
    print "2. Look for clues"

    option = raw_input("-> ")
    if option == "1":
        flashDrive()
    if option == "2":
        BrokeComputer = "True"
        print "You find tracks.. that look like shoe marks. So you follow them.\n"
        time.sleep(3)
        print "You find a house."
        time.sleep(1)
        print "In front of the house, there is a mysterious creature that you can't identify at first..."
        time.sleep(2)
        print "Curiously, you walk closer to it, and it starts engaging!"
        time.sleep(2)
        preFight()


# Check Surroundings
def oneSurrounding():
    HasComputer = "False"
    print "You look around and you see a creature coming..."
    time.sleep(3)
    preFight()

# Where am I ?
def oneWalk():
    os.system('clear')
    print "You stand up and are left with two options..."
    print "1) Check Surroundings"
    print "2) Walk straight in hope..."

    option = int(raw_input("-> "))
    if option == 1:
        oneSurrounding()
    elif option == 2:
        oneFind()
    else:
        oneWalk()

# Found Computer

def oneFind():
    HasComputer = "True"
    print "You find a Laptop on the ground, covered in dirt laying behind a tree."
    time.sleep(1)
    print "..."
    time.sleep(3)
    print "You open the computer and try to connect to WiFi\n"
    print "1) Break Laptop"
    print "2) Wait... "

    option = int(raw_input("-> "))
    if option == 1:
        madeNoise()
        BrokeComputer = "True"
    elif option == 2:
        oneWait()

# Set Computer To true

def madeNoise():
    HasComputer = "False"
    print "YOU MADE NOISE! And you hear something creeping up behind you\n"
    print "1. Continue"
    option = raw_input("-> ")
    if option == "1":
        preFight()

def oneWait():
    HasComputer = "True"
    print "..."
    time.sleep(2.5)
    print "You hear something creeping up behind you"
    time.sleep(1)
    print "You turn around... and realize you just"
    time.sleep(2)
    print " "
    preFight()

def preFight():
    global enemy
    print "Encountered an enemy..."
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = SkeletonAI
    else:
        enemy = ZombieAI
    print "%s! You can try to \n" % enemy.name
    print "1. Dodge"
    print "2. Fight!"
    option = int(raw_input("-> "))
    if option == 1:
        dodge = random.randint(1, 2)
        if dodge == 3:
            print "You dodge the %s!" % enemy.name
        else:
            print "You missed! Prepare to fight..."
            time.sleep(1)
            fight()
    if option == 2:
        fight()

def fight():
    os.system('clear')
    print "%s       vs      %s" % (PlayerIG.name, enemy.name)
    print "Your Health: %d/%d     %s Health: %i/%i" % (PlayerIG.health, PlayerIG.maxHealth, enemy.name, enemy.health, enemy.maxHealth)
    print "Potions: %i\n" % PlayerIG.pot
    print "1. Attack"
    print "2. Drink potion"
    print "3. Run"

    option = (raw_input("-> "))
    if option == "1":
        attack()
    elif option == "2":
        usePotion()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system('clear')
    PAttack = random.randint(PlayerIG.base_attack / 2, PlayerIG.base_attack)
    EAttack = random.randint(PlayerIG.base_attack / 2, PlayerIG.base_attack)
    if PAttack == PlayerIG.base_attack / 2:
        print "You missed!"
    else:
        enemy.health -= PAttack
        print "You dealt %i damage" % PAttack
    time.sleep(0.8)
    if enemy.health <= 0:
        win()
    os.system('clear')
    if EAttack == enemy.attack/2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy dealt %i damage" % EAttack
    time.sleep(0.8)
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()

def usePotion():
    if PlayerIG.pot == 0:
        print "You don't have any potions left!"
    else:
        PlayerIG.health += 50
        if PlayerIG.health > PlayerIG.maxHealth:
            PlayerIG.health = PlayerIG.maxHealth
        print "You drank a potion"
        PlayerIG.pot = PlayerIG.pot - 1
    time.sleep(1)
    fight()

def run():
    runnum = random.randint(0, 1)
    if runnum == 2:
        print "You have succesfully ran away!"
        start1()
    else:
        print "You have failed to get away!"
        time.sleep(1)
        os.system('clear')
        EAttack = random.randint(PlayerIG.base_attack / 2, PlayerIG.base_attack)
        if EAttack == enemy.attack/2:
            print "The enemy missed!"
        else:
            PlayerIG.health -= EAttack
            print "The enemy dealt %i damage" % EAttack
        option = raw_input(' ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()

def win():
    PlayerIG.gold += enemy.goldgain
    PlayerIG.pot = PlayerIG.pot + 1
    enemy.health = enemy.maxHealth
    print "You have defeated the %s!" % enemy.name
    print "You found %i gold & 1 Potion!\n" % enemy.goldgain
    print "1. Search the corpse"
    if enemy.name == Zombie:
        print "2. Eat the meat"
    else:
        print " "
    option = raw_input("-> ")
    if option == "1" and BrokeComputer == "True" or hasFlashDrive == "True":
        os.system('clear')
        print "You find a cellphone... with '5%' battery."
        time.sleep(2)
        print "You have 2 options:\n"
        print "1. Call Mom"
        print "2. Call 911"
        print ""
        option = raw_input("-> ")
        if option == "1":
            callMom()
        if option == "2":
            callCops()
    elif option == "1":
        flashDrive()
    if option == "2":
        dead()
    else:
        win()
def callCops():
    os.system('clear')
    print "RING!"
    time.sleep(2)
    print "RING!"
    time.sleep(2)
    print "RING!"
    time.sleep(1)
    print "911: 911 Whats your Emergency?"
    time.sleep(3)
    print "%s: I NEED HELP!" % PlayerIG.name
    time.sleep(3)
    print "911: Please calm down, and tell me whats going on."
    time.sleep(3)
    print "%s: I'm stranded... I have no clue where I am" % PlayerIG.name
    time.sleep(3)
    print "911: Try to explain your surroundings, anything that would help us locate you"
    time.sleep(3)
    print "%s: I just see.. I just see Trees. I'm in a forest... please help" % PlayerIG.name
    time.sleep(3)
    print "911: Just stay on the line as we track down your locati----"
    time.sleep(3)
    print "- The call drops..."
    time.sleep(2)
    print " "
    print "You anxiously wait, and fall asleep for what feels like..."
    time.sleep(4)
    print "30 minutes"
    print(3)
    rescuedEnding()

def callMom():
    os.system('clear')
    print "RING!"
    time.sleep(2)
    print "RING!"
    time.sleep(2)
    print "RING!"
    answer = random.randint(1, 2)
    if answer == 1:
        time.sleep(0.5)
        print "Mom: Hello?"
        time.sleep(3)
        print "%s: Mom! It's me, %s" % (PlayerIG.name, PlayerIG.name)
        time.sleep(3)
        print "%s: I am lost.. you need to come get me..." % PlayerIG.name
        time.sleep(3)
        print "Mom: Where are you?!"
        time.sleep(3)
        print "%s: I don't know! Track my nu---" % PlayerIG.name
        time.sleep(2)
        print "- The phone dies."
        time.sleep(2)
        print "You start freaking out, feeling stressed, and anxious if anyone will ever come..."
        time.sleep(3)
        print "You pass out... and wake up an hour later."
        rescued = random.randint(1, 2)
        if rescued == 1:
            time.sleep(5)
            rescuedEnding()
        elif rescued == 2:
            time.sleep(5)
            notRescued()
    elif answer == 2:
        time.sleep(3)
        print "The call drops..."
        time.sleep(3)
        print "You try to call again but..."
        time.sleep(3)
        print "The phone dies."
        time.sleep(3)
        print "You start freaking out, feeling stressed, and anxious if anyone will ever come..."
        time.sleep(3)
        print "You pass out... and wake up an hour later."
        time.sleep(5)
        notRescued()

def rescuedEnding():
    os.system('clear')
    print "You wake up to a loud sound coming from the distance..."
    time.sleep(3)
    print "You get, up and realize it's a helicopter...\n"
    time.sleep(4)
    print "CONGRATULATIONS %s!" % PlayerIG.name
    print "You have succesfully completed this Adventure"
    time.sleep(3)
    ending()

def notRescued():
    os.system('clear')
    print "You wake up from a loud noise around you.."
    time.sleep(1)
    print "You get, up and realize it's horde of Zombies..\n"
    print " "
    time.sleep(2)
    print "RIP, %s" % PlayerIG.name
    print "You have unsuccesfully completed this Adventure"
    return

def flashDrive():
    hasFlashDrive = "True"
    if HasComputer == "True":
        print "You plug the flash into the computer, and wait for the drivers to download in order to search the drive\n"
        time.sleep(3)
        os.system('clear')
        print "You open the drive and find a program called 369.exe\n"
        print "1. Open the program"
        print "2. Close the computer, and continue walking"
        option = int(raw_input("-> "))
        if option == 1:
            openProgram()
        if option == 2:
            closeComp()
    elif HasComputer == "True" and BrokeComputer == "True":
        print "You remember you broke the computer... and you can't use the flashdrive, the only hope you had of survival."
        time.sleep(0.3)
        print "..."
        time.sleep(0.2)
        print "..."
        time.sleep(3)
        dead()
    else:
        print "You wonder why you have a mysterious flash drive..."
        time.sleep(1)
        print "So you start looking around"
        oneFind()

def openProgram():
    os.system('clear')
    print "Loading..."
    time.sleep(2)
    print "password:"
    option = raw_input("-> ")
    if option == "369":
        programOpen()

def programOpen():
    ending()

def dead():
    print "You have died!"
    time.sleep(2)
    endingLose()


## ENDING RESULT
def endingRandom():
    print "So... I see you like to take risks..."
    time.sleep(3)
    print "Gamble your life away..."
    time.sleep(3)
    print "Interesting...\n"
    time.sleep(3)
    print "Good luck in the future xD\n"
    time.sleep(1)
    print "ROLLING DICE"
    ending = random.random(1, 3)
    if ending == 1:
        endingWin()
    elif ending == 2:
        endingLose()
    else:
        endingConfuse()

# END = WIN (1)
def ending():
    os.system('clear')
    print "You won (This obviously isn't gonna be the actual ending.)"
    print "Congratulations %s! You made it safely back to CodeDay :)" % PlayerIG.name
    pass

# END = LOSE (2)
def endingLose():
    pass

# END = CONFUSE (3)
def endingConfuse():
    start1()
    print "Yet again? Kappa"

def shop():
    os.system('clear')
    print "Welcome to the shop!"
    print "What would you like to buy? \n"
    print "1) Survivor Sword"
    print "back"
    print " "
    option = raw_input('-> ')

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            PlayerIG.currentWeap = "Survivor Sword"
        else:
            print "You do not have enough gold!"
            option = raw_input("Press enter")
            shop()
    elif option == "back":
        start1()

    else:
        os.system('clear')
        print "That item does not exist"
    option = raw_input("Press enter")
    start1()

def leaveShop():
    pass
main()
