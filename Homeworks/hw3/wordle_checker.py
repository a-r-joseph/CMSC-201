"""
File:    wordle_checker.py
Author:  Abby Joseph
Date:    2/26/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input of a solution word and a guess word to simulate the game
             Wordle. The output displays y, g, or _ to indicate if the letter is in the word and
             if it is in the correct position.
"""


if __name__ == '__main__':

    solution_word_in = input('Enter the solution word: ')

    if len(solution_word_in) == 5:
        guess_word_in = input('Enter the guess word: ')
        if len(guess_word_in) == 5:
            for i in range(len(guess_word_in)):
                if guess_word_in[i] == solution_word_in[i]:
                    print('g', end=' ')
                elif guess_word_in[i] in solution_word_in:
                    print('y', end=' ')
                else:
                    print('_', end=' ')
        else:
            print('Please only enter words that are 5 letters long.')
    else:
        print('Please only enter words that are 5 letters long.')
