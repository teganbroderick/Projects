#!/usr/bin/env python3
#Tegan Broderick, 20190815
#Hangman game that uses words from the SOWPODS dictionary.
#Exercise 32 from practicepython.org

import random

def import_dictionary(path):
    """Function opens SOWPODS dictionary txt file, reads lines, creates a dictionary list, and returns the dictionary"""
    dictionary= []
    with open(path, 'r') as f:
      line = f.readline().strip() #strip \n character from end of line
      while line: #while there are lines left to read
        dictionary.append(line)
        line = f.readline().strip()
    return dictionary

def randomword(wordlist):
    """Function generates a random integer, finds the word located at this integer position in the wordlist, and returns this random word"""
    integer = random.randrange(0,len(wordlist))
    randomword = wordlist[integer]
    return randomword

def game(word, word_list, output_list, guess_list, alphabet_list, count):
    """Function takes user input for a letter, appends letter to guesslist for referencing, and analyses whether letter is in the random word."""
    """ If the letter is in the random word, function adds the letter to the output list and prints the output word."""
    """ If the letter is not in the random word, the function prints the hangman drawing associatd with how many turns the user has taken."""
    while (count >= 1) and ("_" in output_list):
        letter = input("Guess your letter: ")
        letter = letter.upper() #convert input to uppercase

        while letter in guess_list or letter not in alphabet_list:
            if letter in guess_list:
                print("You already guessed that letter. Try again.")
            elif letter not in alphabet_list:
                print("Invalid input. Try again")
            letter = input("Guess your letter: ")
            letter = letter.upper() #convert input to uppercase

        guess_list.append(letter) #append letter to guess list for future reference

        if letter in word_list:
            for i in range(0,len(word_list)):
                if letter == word_list[i]:
                    output_list[i] = letter

            output_word = "".join(output_list) #concatenate contents of list into output_word string
            print("Word:", output_word)
            print()

            if "_" not in output_list:
                print("You won!")

        else:
            print("Letter not found!")
            count -= 1
            drawhangman(count, word)
            output_word = "".join(output_list) #needed to generate output word if first try is wrong
            print("Word:", output_word)
            print()

def drawhangman(number, correctword):
    if number == 5:
        print("________")
        print("|      |")
        print("|      o")
        print("|         ")
        print("|         ")
        print("|_________")
    elif number == 4:
        print("________")
        print("|      |")
        print("|      o")
        print("|      |")
        print("|         ")
        print("|_________")
    elif number == 3:
        print("________")
        print("|      |")
        print("|      o")
        print("|     /|")
        print("|         ")
        print("|_________")
    elif number == 2:
        print("________")
        print("|      |")
        print("|      o")
        print("|     /|\\")
        print("|         ")
        print("|_________")
    elif number == 1:
        print("________")
        print("|      |")
        print("|      o")
        print("|     /|\\")
        print("|     /   ")
        print("|_________")
    elif number == 0:
        print("________")
        print("|      |")
        print("|      o")
        print("|     /|\\")
        print("|     / \\")
        print("|_________")
        print()
        print("You lose!!! The correct word was " + correctword)

if __name__ == "__main__":
    dictionary = import_dictionary('/Users/teganbroderick/Documents/Coding/Word Game/sowpods.txt')
    repeat = "YES"

    while repeat == "YES" or repeat == 'yes' or repeat == 'Y':

        #word setup
        word = randomword(dictionary) #get random word
        word_list = list(word) #split word (string) into a list of characters
        output_word = len(word)*"_" # Make 'blank' string of spaces the same length as the random word
        output_list = list(output_word) #Convert 'blank' string into 'blank' list of spaces the same length as the random word, which holds letters as the game progresses
        guess_list = [] #list for letters that user has guessed
        alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] #reference list for input
        count = 6 #total number of incorrect guesses allowed
        repeat = "yes"

        print("Welcome to Hangman!")
        #empty hangman drawing
        print("________")
        print("|      |")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|_________")
        print()

        print("Word: ", output_word)

        #call game
        game(word, word_list, output_list, guess_list, alphabet_list, count)

        #repeat option
        repeat = input("Do you want to play again? yes or no: ")
        print()
