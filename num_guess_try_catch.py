#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 15, 2022
# This program checks if a user's integer guess is correct to the computer's generated number
# and additionally checks if the user's input is an integer

# imports random
import random


def main():
    # this function uses a try statement

    # assigns a random number from 0-9 to the secret_number variable
    secret_number = random.randint(0, 9)

    # asks the user for input (their guess)
    print("The secret number is between 0-9")
    # had to remove "int" or "float" when asking for input here
    user_guess = input("Enter your guess: ")

    # process and output
    try:
        user_guess = int(user_guess)
        # check if the user's guess matches secret_number and output if statement is correct
        if secret_number == user_guess:
            print("Your guess is right!")

        # else, if the user guessed incorrectly
        else:
            print(f"You guessed incorrectly, The correct answer was {secret_number}")
    # similar to an else statement, if an integer is not inputted...
    except:
        print(f"{user_guess} is not an integer. Please enter an integer")


if __name__ == "__main__":
    main()
