import random
import time

try_again = True;

while try_again:

    print("Greetings, Space General! :)")
    time.sleep(2) # waits 2 seconds
    print("It seems there are 3 aliens ahead of you preparing to attack . . .")
    time.sleep(2) # waits 2 seconds
    user_answer = int(input("Which one will you choose to attack? Choose wisely.\n"))

    alien_color = random.randint(1,3)

    if user_answer == 1:
        if alien_color == 1:
            print("Your alien was green! You earn 5 points!")
        elif alien_color == 2:
            print("Your alien was yellow. You earn 10 points.")
        elif alien_color == 3:
            print("Your alien was blue. You earn 10 points.")

    elif user_answer == 2:
        if alien_color == 1:
            print("Your alien was yellow. You earn 10 points.")
        elif alien_color == 2:
            print("Your alien was blue. You earn 10 points.")
        elif alien_color == 3:
            print("Your alien was green! You earn 5 points!")

    elif user_answer == 3:
        if alien_color == 1:
            print("Your alien was blue. You earn 10 points.")
        elif alien_color == 2:
            print("Your alien was green! You earn 5 points!")
        elif alien_color == 3:
            print("Your alien was yellow. You earn 10 points.")

    try_again = input("Would you like to try again? (y/n) ")
    if try_again == "y":
        continue
    else:
        print("Thanks for playing!")
        break
