import random as rand
import time
import os

clear = lambda: os.system("clear")
clear()

print("""
Task:-
    GUESS THE NUMBER
Rules:-
    1)The random number will be between 1 to 50.
    2) The number is an integer, so entering a decimal will be wrong.
    3) You will get 5 chances.
""")
time.sleep(5)
clear()

n = rand.randrange(1,50)
lives = 5

while True:
    try:
        clear()
        print(f"""
Chances Left -->  {lives}

        """)

        guess = int(input("Take a guess: "))

        if guess == n:
            print("CORRECT ANSWER!!!")
            break
        elif guess < n:
            print("The guessed number is small")
            lives -= 1
        else:
            print("The guessed number is greater")
            lives -= 1

    except ValueError:
        print("You have entered a decimal number")
        lives -= 1

    if lives == 0:
        print("\nGame Over")
        print(f"The number was  -->  {n}")
        time.sleep(5)
        break

    print(f"You are left with {lives} chances\n")
    time.sleep(2.5)
