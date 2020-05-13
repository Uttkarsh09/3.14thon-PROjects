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
    log = []
    if choice == 1:
        limit = 10
        word = "EASY"
        lives = 4
    elif choice == 2:
        limit = 50
        word = "MEDIUM"
        lives = 5
    else:
        lives = 6
        word = "DIFFICULT"
        limit = 100

    print(f"""
                                {word}
        Task:-
            GUESS THE NUMBER
        Rules:-
            1)The random number will be between 1 to {limit}.
            2) The number is an integer, so entering a decimal will be wrong.
            3) You will get {lives} chances.
        """)
        
    time.sleep(5)
    clear()

    n = rand.randrange(1,limit)

    while True:
        try:
            clear()
            print(f"""
    Chances Left -->  {lives}

            """)

            guess = int(input("Take a guess: "))
            log.append(guess)

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
            print("Your inputs -->  ",log)
            time.sleep(5)
            break

        print(f"You are left with {lives} chances\n")
        time.sleep(2.5)

eStart(choice)

#version 2 of the prototype