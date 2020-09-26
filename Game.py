import time
import sys
import os
from Player import Player

def clear(lines):
    for i in range(lines):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()
print("""
---------------------------------------------
Welcome to my test game!
This game is based on the Cyberpunk universe.
I hope you enjoy it!
---------------------------------------------
""")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

loop = 0
while loop == 0:
    print("""------------------------------------------------------------------------
What's your street name?
    
Think wisely, the name you choose here can't be changed during the game.
------------------------------------------------------------------------
""")

    name = input().strip()

    print(f"""
Are you sure you want your name to be {name}?
""")

    while True:
        answer = input().lower().strip()
        if answer == "no":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif answer == "yes":
            loop += 1
            break
        else:
            print("""
------------------------
Please answer yes or no.
------------------------
""")
            time.sleep(1)
            clear(6)
            continue

os.system('cls' if os.name == 'nt' else 'clear')

attr_points = 8
attr = ["body", "intelligence", "reflexes", "technical", "cool", "bod", "int", "ref", "tech",]

player = Player(name)

while True:

    print(f"""-----------------------------------------------------------------------
Please customize your characters' attributes.
You have {attr_points} points left.
to spend.
- Body: {player.bod}
- Intelligence: {player.int}
- Reflexes: {player.ref}
- Technical: {player.tech}
- Cool: {player.cool}
(Type the attribute you want to increase and the value you want to add)
-----------------------------------------------------------------------
""")
    if attr_points == 0:
        break

    while True:
        answer = input().lower().strip().split()
        if len(answer) == 2 and answer[0] in attr:
            try:
                answer[1] = int(answer[1])
                if answer[1] <= attr_points and answer[1] > 0:
                    if player.see_change(answer) <= 10:
                        player.change(answer)
                        attr_points -= answer[1]
                        break
                    else:
                        print("Each attribute has a maximum value of 10!")
                        time.sleep(2)
                        clear(2)
                else:
                    print("That number is too big, please try another one.")
                    time.sleep(2)
                    clear(2)

            except ValueError:
                print("Invalid input, please type a number following the attribute!")
                time.sleep(2)
                clear(2)
        else:
            print("Invalid input, please follow the instructions.")
            time.sleep(2)
            clear(2)
            
    os.system('cls' if os.name == 'nt' else 'clear')




time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


print("""-----------------------------
Before we get started, choose
your background.
-----------------------------
(A) Street Kid
(B) Nomad
(C) Corporate
""")


test = 0
while test == 0:
    answer = input().lower().strip()
    if answer == "a":
        print("""
You chose the Street Kid path.
        """)
        test += 1
    elif answer == "b":
        print("""
You chose the Nomad path.
        """)
        test += 1
    elif answer == "c":
        print("""
You chose the Corporate path.
        """)
        test += 1
    else:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()
        pass

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print("Good luck surviving Night City.")
time.sleep(3)





