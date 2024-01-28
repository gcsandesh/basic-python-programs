import random
import os

MAX_NUMBER_OF_TRIES = 4


def main():
    print("\nWelcome to Guess the Animal game.\n")

    animals_file = open("./guess_the_animal/list_of_animals.txt", "r")
    list_of_animals = animals_file.read().splitlines()
    animals_file.close()

    animal = random.choice(list_of_animals)

    remaining_chances = MAX_NUMBER_OF_TRIES
    revealed_letters = list("_" * len(animal))

    while remaining_chances > 0:
        print(str(remaining_chances) + " chances remaining")
        print(" ".join(revealed_letters))

        input_str = input().lower()

        os.system("clear || cls")  # clears the terminal after every input

        index_of_character = animal.lower().find(input_str)

        if index_of_character < 0:
            remaining_chances -= 1
        else:
            del revealed_letters[index_of_character]
            revealed_letters.insert(index_of_character, animal[index_of_character])

        if "".join(revealed_letters) == animal:
            print("You guessed the animal!")
            print(animal)
            return
    print("You could not guess the animal.")
    print("The animal was: " + animal)


if __name__ == "__main__":
    main()  # does not run if the file is imported
