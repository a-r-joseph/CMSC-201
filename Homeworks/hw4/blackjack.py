"""
File:    blackjack.py
Author:  Abby Joseph
Date:    3/5/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program lets the user play a game of blackjack where they bet money until they go
             bankrupt or no longer want to play.
"""

import sys
from random import randint, seed
if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == '__main__':

    continue_game = input('Do you wish to continue to play? ')
    money_units = 100

    while (continue_game.lower() == 'yes') and (money_units > 0):
        bet_value = int(input('How much do you want to bet? '))
        if bet_value > money_units:
            print(f'You only have {money_units} dollars. Please only bet what you can pay.')
        elif bet_value <= 0:
            print('Please make a valid bet to continue the game.')
        else:
            card_values_list = [str(randint(1, 13)), str(randint(1, 13))]
            print('Your card values are ' + ' '.join(card_values_list))
            card_total = int(card_values_list[0]) + int(card_values_list[1])
            if 16 <= card_total <= 21:
                money_units = money_units + bet_value
                print(f'You win {bet_value} dollars. You now have {money_units} dollars.')
            else:
                money_units = money_units - bet_value
                print(f'You lose {bet_value} dollars. You now have {money_units} dollars.')
        if money_units == 0:
            print('You went bankrupt...')
        else:
            continue_game = input('Do you wish to continue to play? ')

    if money_units > 0:
        print(f'You ended up with {money_units} dollars.')
