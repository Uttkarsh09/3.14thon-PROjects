import random as rand
import time
import os
from pynput import keyboard

clear = lambda: os.system("clear")
clear()

print("""Choose the difficulty...
        1) Easy
        2) Medium
        3) Difficult
""")

def take_choice():
    try:
        n = int(input("Enter your choice: "))
        if not (n >= 1 and n <=3):
            raise ValueError
    except ValueError:
        print("Oops you have not entered a number between 1 and 3")
        take_choice()
    return n

choice = take_choice()



def eStart(choice):
    if choice == 1:
        print("""
                                EASY
        Task:-
            GUESS THE NUMBER
        Rules:-
            1)The random number will be between 1 to 10.
            2) The number is an integer, so entering a decimal will be wrong.
            3) You will get 5 chances.
        """)
        time.sleep(5)
        clear()

        n = rand.randrange(1,10)
        lives = 4

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

    elif choice == 2:
        print("""
                                MEDIUM
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

    elif choice == 3:
        print("""
                                DIFFICULT
        Task:-
            GUESS THE NUMBER
        Rules:-
            1)The random number will be between 1 to 100.
            2) The number is an integer, so entering a decimal will be wrong.
            3) You will get 5 chances.
        """)
        time.sleep(5)
        clear()

        n = rand.randrange(1,100)
        lives = 6

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
            
eStart(choice)