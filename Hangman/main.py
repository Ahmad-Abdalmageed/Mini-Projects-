# This is a simple Hangman Game which is implemented in Python 3.7.3
#
# Game Rules are as follows :
# 1- The program choose a random word from the list
# 2- User Guesses a character from the word, for every correct choice
#     the character`s position appears
# 3- There are a number of trials before game over
#
# Imports
from pandas import read_csv as read
from numpy import array as array
from numpy.random import choice as np_choice
# We need to import the words text file

file = read('words.txt')
words = array(file.iloc[:, 0])

# Used Functions
def getWord(wordList):
    choice = np_choice(wordList)
    return choice



if __name__ == '__main__':
    print("Welcome To HANGMAN 0.1", "You`re given only 5 trials to guess the right word",sep= '\n')
    print("\n")
    print("Otherwise", "You LOSE", sep='\n')






