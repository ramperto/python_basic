#!/usr/bin/env python

#source = """You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
#While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters."""

#print(source.lower())

import string

def checkio(word):

    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1

    dictionary = sorted(dictionary.items(), 
                        reverse=True, 
                        key=lambda x: x[1])

    for position in range(0, 26):
        print dictionary[position]
        if position != len(dictionary) - 1:
            if dictionary[position + 1][1] < dictionary[position][1]:
                break

checkio("one")
