"""
    Guess the number game.
    User will input the number and try to guess the number.
"""
import random

NUMBER_RANGE_START = 1
NUMBER_RANGE_END = 100

print("\nGuess the number!\n")

number = random.randint(
    NUMBER_RANGE_START, NUMBER_RANGE_END
)  # returns a random integer from specified range, including both start and end


def check_number(number, input_number):
    if number == input_number:
        return True
    elif number > input_number:
        print(f"The number is greater than {input_number}.")
        return False
    elif number < input_number:
        print(f"The number is less than {input_number}.")
        return False


def take_input_from_user():
    return int(input("Enter your guess: "))


attempts = 0

while True:
    attempts += 1
    input_number = take_input_from_user()

    if check_number(number, input_number):
        print("\nYou guessed the number!\n")
        print(f"Number: {number}\nAttempts: {attempts}")
        break
