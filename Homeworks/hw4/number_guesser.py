"""
File:    number_guesser.py
Author:  Abby Joseph
Date:    3/5/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program generates a random number and lets the user guess the number until they
             get it correct.
"""

import sys
from random import randint, seed
if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == '__main__':

    solution_num = randint(1, 100)
    guess_num_in = int(input('Guess a number between 1 and 100. '))
    guess_count = 1

    while guess_num_in != solution_num:
        if guess_num_in < solution_num:
            print('Your guess is too low.')
            guess_count += 1
        else:
            print('Your guess is too high.')
            guess_count += 1
        guess_num_in = int(input('Guess a number between 1 and 100. '))

    print(f'You guessed the value! It took you {guess_count} steps. ')
