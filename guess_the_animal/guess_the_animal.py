import random
import os

MAX_NUMBER_OF_TRIES = 4


def main():
    print("\nWelcome to Guess the Animal game.\n")

    animals_file = open("./guess_the_animal/list_of_animals.txt", "r")
    list_of_animals = animals_file.read().splitlines()
    animals_file.close()

    animal = remove_spaces_from_string(random.choice(list_of_animals))

    remaining_chances = MAX_NUMBER_OF_TRIES
    revealed_letters = list("_" * len(animal))
    remaining_letters = list(animal)

    while remaining_chances > 0:
        print("remaining letters: " + "".join(remaining_letters) + "\n")

        print(str(remaining_chances) + " chances remaining")
        print(" ".join(revealed_letters))

        input_str = input().lower()

        os.system("clear || cls")  # clears the terminal after every input
        if len(input_str) == 1 and input_str.isalpha():
            index_of_character = "".join(remaining_letters).lower().find(input_str)

            if index_of_character < 0:
                if "".join(revealed_letters).find(input_str) >= 0:
                    print("You already guessed that letter.")
                else:
                    remaining_chances -= 1
            else:
                while index_of_character >= 0:
                    del_and_insert(
                        revealed_letters,
                        index_of_character,
                        animal[index_of_character],
                    )
                    del_and_insert(remaining_letters, index_of_character, "_")

                    index_of_character = (
                        "".join(remaining_letters).lower().find(input_str)
                    )

            if "".join(revealed_letters) == animal:
                print("You guessed the animal!")
                print(animal)
                return
        else:
            print("Enter a single letter.")

    print("You could not guess the animal.")
    print("The animal was: " + animal)


def remove_spaces_from_string(string):
    return string.replace(" ", "")


def del_and_insert(list, index, character):
    del list[index]
    list.insert(index, character)


if __name__ == "__main__":
    main()  # does not run if the file is imported
