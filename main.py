"""
NATO Alphabet

Author: Alan
Date: September 13th 2024
Update: September 17th 2024

This script prints a list of words of the phonetic alphabet based on the user's input.
"""

import pandas

# Access data from a csv file.
nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create new dictionary using the letter and the code
new_dict = {row.letter:row.code for (index, row) in nato_alphabet_data.iterrows()}

def generate_nato_word_list():

    # Ask user for a word
    word = input("Input your name:\n").upper()

    try:

        # Create new list using each letter of the word for a new dictionary
        word_list = [new_dict[letter] for letter in word]

        # Prints the list of words
        print(word_list)

    except KeyError:

        print("Sorry, only letters in the alphabet, please.")
        generate_nato_word_list()

generate_nato_word_list()
