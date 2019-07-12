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
from numpy.random import choice as np_choice
# We need to import the words text file

file = read('words.txt')
words = [word for word in file.iloc[:, 0] if len(word) >= 4]
hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Used Functions
def get_word(word_list):
    choice = np_choice(word_list)
    return choice, len(choice)


def game_start():
    print("Welcome To HANGMAN 0.1", "You`re given only 5 wrong guesses", sep='\n')
    print("Otherwise, You LOSE")
    print(hangmanPics[0])


def game_processes(size, word):
    hidden_word = [" _ " for point in range(size)]

    print(''.join(hidden_word))
    hang = 1

    while hang != 6:
        guess = input("Enter a guess :")
        if guess in word:
            pos = word.find(guess)
            hidden_word[pos] = guess
            print('\n'+hangmanPics[hang-1])
            print(''.join(hidden_word))

        elif guess not in word:
            print(hangmanPics[hang])
            hang += 1
    else:
        print(hangmanPics[6]+'\n')
        print("GAME OVER")


if __name__ == '__main__':
    game_start()
    chosen_word, length = get_word(words)
    print(chosen_word)
    game_processes(length, chosen_word)

















