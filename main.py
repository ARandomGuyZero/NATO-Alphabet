"""
NATO Alphabet

Author: Alan
Date: September 13th

This script prints a list of words of the phonetic alphabet based on the user's input.
"""

import pandas

# Access data from a csv file.
nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create new dictionary using the letter and the code
new_dict = {row.letter:row.code for (index, row) in nato_alphabet_data.iterrows()}

# Ask user for a word
word = input("Input your name:\n").upper()

# Create new list using each letter of the word for a new dictionary
word_list = [new_dict[letter] for letter in word]

# Print new list of words
print(word_list)