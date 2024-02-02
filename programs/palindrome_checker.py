"""
    Program to take a word as input from the user and check if the word is a palindrome or not.
"""


def check_palindrome(word):
    """
    :param word: string - word which is to be checked if it is a palindrome or not
    :return: boolean - True if palindrome and False if not palindrome

    Function that takes the input word from the user and returns if the word is a palindrome or not.
    """
    isPalindrome = False

    reverse_word = word[::-1]

    if word.lower() == reverse_word.lower():
        isPalindrome = True

    return isPalindrome


print("\nPalindrome Checker\n")
input_word = input("Enter a word: ")

if check_palindrome(input_word):
    print(f"{input_word} is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")
