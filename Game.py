import time
import sys
import os

print("""
-----------------------------
Welcome to my test game!
This game is based on the
Cyberpunk universe.
I hope you enjoy it!
-----------------------------
""")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

loop = 0
while loop == 0:
    print("""
-----------------------------
What's your street name?
    
Think wisely, the name you
choose here can't be changed
during the game.
-----------------------------
""")

    name = input().strip()

    print(f"""
-----------------------------
Are you sure you want your
name to be {name}?
-----------------------------
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
-----------------------------
Please answer yes or no.
-----------------------------
""")
            time.sleep(1)
            for i in range(6):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.flush()
            continue
        os.system('cls' if os.name == 'nt' else 'clear')


print("""
-----------------------------
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





