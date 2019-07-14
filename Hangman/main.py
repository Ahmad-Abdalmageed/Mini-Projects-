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

# Hangman Pic-Art
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
    """
     Choosing a random word from a given list
    """
    choice = np_choice(word_list)
    return choice, len(choice)


def game_start():
    """
    Prints the first lines of the structure of the game
    """
    print("Welcome To HANGMAN 0.1", "You`re given only 5 wrong guesses", sep='\n')
    print("Otherwise, You LOSE")
    print(hangmanPics[0])


def find(word, character):
    """
    Finds the occurrences of a certain character in a certain word
    and returns a list of all the occurrences`s indices
    """
    occurrences = [position for position, char in enumerate(word) if char == character]
    return occurrences


def game_processes(word, size):
    """
    The main game function which takes guesses and count the user
    attempts, prints the hangman pic-art and congratulates the
    user for finishing the game
    """
    # Hide the chosen word then print it
    hidden_word = [' _ ' for item in range(size)]
    print(''.join(hidden_word))
    hang = 0

    # while hang != 6:
    #     guess = input("Enter a guess :")
    #
    #     # Winning situation
    #     if guess in word:
    #         positions = find(word, guess)
    #         for position in positions:
    #             hidden_word[position] = guess
    #
    #         print('\n' + hangmanPics[hang-1])
    #         print(''.join(hidden_word))
    #
    #     # Losing situation
    #     elif guess not in word:
    #         print(hangmanPics[hang])
    #         print(''.join(hidden_word))
    #         hang += 1
    # else:
    #     if ''.join(hidden_word) == word:
    #         print("YOU WON")
    #
    #     else:
    #         print(hangmanPics[6] + '\n')
    #         print("GAME OVER")

    while hang < 5:
        guess = input("Take a guess :")
        goal = ''.join(hidden_word)
        if guess in word:
            positions = find(word, guess)
            for position in positions:
                hidden_word[position] = guess
            print(''.join(hidden_word), hangmanPics[hang], sep='\n')
        elif guess not in word:
            hang += 1
            print(hangmanPics[hang], ''.join(hidden_word), sep='\n')
        elif goal == str(word):
            print("WOW, YOU WON !!!")
            break
    else:
        print(hangmanPics[6] + '\n')
        print("GAME OVER")


if __name__ == '__main__':

    game_start()
    chosen_word, length = get_word(words)

    print(chosen_word)
    game_processes(chosen_word, length)


















