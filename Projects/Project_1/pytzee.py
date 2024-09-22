"""
File:    pytzee.py
Author:  Abby Joseph
Date:    4/4/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program simulates the game yahtzee and allows the user to earn points based on
             their dice rolls.
"""

import random

TOTAL_DICE = 5
DICE_FACES = 6

SCORING_METHODS = [['count 1', 'count one'], ['count 2', 'count two'], ['count 3', 'count three'],
                   ['count 4', 'count four'], ['count 5', 'count five'], ['count 6', 'count six'],
                   ['3 of a kind', 'three of a kind'], ['4 of a kind', 'four of a kind'],
                   ['full house', 0], ['small straight', 0], ['large straight', 0], ['pytzee', 0],
                   ['chance', 0]]

TWO_OF_A_KIND = 2
THREE_OF_A_KIND = 3
FOUR_OF_A_KIND = 4
FIVE_OF_A_KIND = 5

TWENTY_FIVE_POINTS = 25
THIRTY_POINTS = 30
FORTY_POINTS = 40
FIFTY_POINTS = 50
HUNDRED_POINTS = 100

CHANCE_INDEX = 12
PYTZEE_INDEX = 11
L_STRAIGHT_INDEX = 10
S_STRAIGHT_INDEX = 9
FULL_HOUSE_INDEX = 8
FOUR_KIND_INDEX = 7
THREE_KIND_INDEX = 6
COUNT_6_INDEX = 5
COUNT_5_INDEX = 4
COUNT_4_INDEX = 3
COUNT_3_INDEX = 2
COUNT_2_INDEX = 1
COUNT_1_INDEX = 0

SEQUENCE_OF_FOUR = 3
SEQUENCE_OF_FIVE = 4


def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    # Appends the list with a random value 1-6 to represent 5 dice rolls
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, DICE_FACES))
    return roll_list


def sort_dice_rolls(dice_rolls):
    """
    :param dice_rolls: a list containing the numbers rolled on each dice
    :return: a list containing the numbers rolled on each dice from least to greatest with doubles
             removed
    """
    for n in range(len(dice_rolls)):
        for i in range(len(dice_rolls)):
            if dice_rolls[i] < dice_rolls[n]:
                if i > n:
                    temp_var = dice_rolls[n]
                    # Swaps the values to put the numbers in numerical order
                    dice_rolls[n] = dice_rolls[i]
                    dice_rolls[i] = temp_var
    for k in range(len(dice_rolls)):
        if k < len(dice_rolls) - 1:
            if dice_rolls[k] == dice_rolls[k + 1]:
                dice_rolls.remove(dice_rolls[k])

    return dice_rolls


def generalize_score_name(scoring_type):
    """
    :param scoring_type: a user-inputted string of the chosen score method
    :return: a simplified name for the scoring method
    """
    if scoring_type.lower() == 'skip':
        return 'skip'
    method = scoring_type.lower()
    # Changes the scoring_type string to a standard string representing the score method
    for i in range(len(SCORING_METHODS)):
        for x in range(len(SCORING_METHODS[0])):
            if SCORING_METHODS[i][x] == method:
                return SCORING_METHODS[i][0]
    return False


def mark_method_used(scoring_type, score_method_unused):
    """
    :param scoring_type: a user-inputted string of the chosen score method
    :param score_method_unused: a list containing bools that represent if the scoring method is
                                unused
    :return: None
    """
    for i in range(len(SCORING_METHODS)):
        # Changes the parallel bool to False to show it has been used
        if scoring_type in SCORING_METHODS[i]:
            score_method_unused[i] = False


def validate_method(dice_rolls, scoring_type):
    """
    :param dice_rolls: a list containing the number rolled on each dice
    :param scoring_type: a user-inputted string of the chosen score method
    :return: a boolean value representing if the scoring method can be used based on the present
             dice rolls
    """
    kind_count = 0
    straight_count = 0
    if scoring_type == 'skip':
        return True
    elif scoring_type not in generalize_score_name(scoring_type):
        return False
    elif 'count' in scoring_type.split():
        for dice in dice_rolls:
            if dice == int(scoring_type.split()[1]):
                return True
        return False
    elif 'kind' in scoring_type.split():
        for dice_side in range(1, DICE_FACES + 1):
            for dice in dice_rolls:
                if dice == dice_side:
                    kind_count += 1
            if kind_count == int(scoring_type.split()[0]):
                return True
            else:
                kind_count = 0
        return False
    elif scoring_type == 'full house':
        # Checks if there is both a pair and a three-of-a-kind to confirm there is a full house
        full_house_list = [False, False]
        for dice_side in range(1, DICE_FACES + 1):
            for dice in dice_rolls:
                if dice == dice_side:
                    kind_count += 1
            if kind_count == THREE_OF_A_KIND and not full_house_list[0]:
                full_house_list[0] = True
            elif kind_count == TWO_OF_A_KIND and not full_house_list[1]:
                full_house_list[1] = True
            kind_count = 0
        if full_house_list == [True, True]:
            return True
        return False
    elif 'straight' in scoring_type.split():
        dice_rolls = sort_dice_rolls(dice_rolls)
        for i in range(len(dice_rolls)):
            if i > 0:
                if dice_rolls[i] == dice_rolls[i - 1] + 1:
                    straight_count += 1
                else:
                    straight_count = 0
        if 'large' in scoring_type.split() and straight_count == SEQUENCE_OF_FIVE:
            return True
        if 'small' in scoring_type.split() and straight_count == SEQUENCE_OF_FOUR:
            return True
        return False
    elif scoring_type == 'chance':
        return True
    elif scoring_type == 'pytzee':
        for dice_side in range(1, DICE_FACES + 1):
            for dice in dice_rolls:
                if dice == dice_side:
                    kind_count += 1
            if kind_count >= FIVE_OF_A_KIND:
                return True
            else:
                kind_count = 0
        return False
    else:
        return False


def check_score_slot(scoring_type, score_method_unused):
    """
    :param scoring_type: a user-inputted string of the chosen score method
    :param score_method_unused: a list containing bools that represent if the scoring method is
                                unused
    :return: a boolean value that represents if the scoring method has already been used
    """
    for i in range(len(SCORING_METHODS)):
        if scoring_type in SCORING_METHODS[i]:
            # Checks if the score method is still unused
            if not score_method_unused[i]:
                return False
    return True


def scoring_string(scoring_type, num_points):
    """
    :param scoring_type: a user-inputted string of the chosen score method
    :param num_points: the number of points scored based on the rolls and the scoring method
    :return: a string acknowledging the method of scoring and the points scored
    """
    if 'count' in scoring_type.split():
        # Confirmation message for scoring through count
        return f'Accepted the {scoring_type.split()[1]}\n'
    elif 'kind' in scoring_type.split():
        if '3' in scoring_type.split():
            return f'You have three of a kind!\n'
        if '4' in scoring_type.split():
            return f'You have four of a kind!\n'
    elif 'chance' == scoring_type:
        return f'You chose chance and get {num_points} points.\n'
    else:
        return f'You have a {scoring_type} and get {num_points} points.\n'


def detect_score(dice_rolls, scoring_type):
    """
    :param dice_rolls: a list containing the number rolled on each dice
    :param scoring_type: a user-inputted string of the chosen score method
    :return: the points scored based on the rolls and the scoring method
    """
    score_count = 0
    if 'count' in scoring_type.split():
        for dice in dice_rolls:
            if dice == int(scoring_type.split()[1]):
                score_count += dice
    elif 'kind' in scoring_type.split():
        score_count = sum(dice_rolls)
    elif scoring_type.lower() == 'full house':
        # Rewards 25 points for scoring through a full house
        score_count = TWENTY_FIVE_POINTS
    elif scoring_type.lower() == 'small straight':
        score_count = THIRTY_POINTS
    elif scoring_type.lower() == 'large straight':
        score_count = FORTY_POINTS
    elif scoring_type.lower() == 'chance':
        score_count = sum(dice_rolls)
    elif scoring_type.lower() == 'pytzee':
        score_count = FIFTY_POINTS
    else:
        return 0
    return score_count


def display_scorecard(scorecard_list):
    """
    :param scorecard_list: A list containing the scores produce by each scoring method
    :return: None
    """
    # Displays a scorecard for the user to see their scores
    print(f'\tScorecard:\n1\'s 2\'s 3\'s 4\'s 5\'s 6\'s \n{scorecard_list[COUNT_1_INDEX]}\t'
          f'{scorecard_list[COUNT_2_INDEX]}\t{scorecard_list[COUNT_3_INDEX]}\t'
          f'{scorecard_list[COUNT_4_INDEX]}\t{scorecard_list[COUNT_5_INDEX]}\t'
          f'{scorecard_list[COUNT_6_INDEX]}\nThree of a kind\tFour of a kind\tFull House\t'
          f'Small Straight\tLarge Straight\tPytzee\tChance \n{scorecard_list[THREE_KIND_INDEX]}\t'
          f'\t\t\t{scorecard_list[FOUR_KIND_INDEX]}\t\t\t\t{scorecard_list[FULL_HOUSE_INDEX]}\t\t\t'
          f'{scorecard_list[S_STRAIGHT_INDEX]}\t\t\t\t{scorecard_list[L_STRAIGHT_INDEX]}\t\t\t\t'
          f'{scorecard_list[PYTZEE_INDEX]}\t\t{scorecard_list[CHANCE_INDEX]}\n')


def ask_score_method(dice_rolls, score_method_unused):
    """
    :param dice_rolls: a list containing the number rolled on each dice
    :param score_method_unused: a list containing bools that represent if the scoring method is
                                unused
    :return: a valid score method that can be used
    """
    # Ask the user which scoring method they want to use
    score_method = input('\nHow would you like to count this dice roll? ')
    score_method = generalize_score_name(score_method)
    while True:
        if score_method:
            scoring_permitted = validate_method(dice_rolls, score_method)
            if scoring_permitted or score_method == 'pytzee':
                scoring_permitted = check_score_slot(score_method, score_method_unused)
                if scoring_permitted or score_method == 'pytzee':
                    return score_method
                else:
                    score_method = input('There was already a score in that slot. \nHow would you '
                                         'like to count this dice roll? ')
                    score_method = generalize_score_name(score_method)
            else:
                score_method = input('Please enter a valid response. \nHow would you like '
                                     'to count this dice roll? ')
                score_method = generalize_score_name(score_method)
        else:
            score_method = input('Please enter a valid response. \nHow would you like '
                                 'to count this dice roll? ')
            score_method = generalize_score_name(score_method)


def play_game(number_rounds):
    """
    :param number_rounds: The number of rounds chosen to play by the user
    :return: None
    """
    score_method_unused = [True, True, True, True, True, True, True, True, True, True, True, True,
                           True]
    score_card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    round_count = 1
    score_count = 0

    while round_count <= number_rounds:
        print(f'***** Beginning Round {round_count} *****')
        print(f'\t Your score is: {score_count}')
        roll_list = roll_dice()
        for roll in roll_list:
            print(f'\t{roll}', end='')
        score_method = ask_score_method(roll_list, score_method_unused)
        if score_method != 'skip':
            points_this_round = detect_score(roll_list, score_method)
            # Adds 100 points instead of 50 if not the first pytzee
            if score_method == 'pytzee':
                if not score_method_unused[PYTZEE_INDEX]:
                    points_this_round = HUNDRED_POINTS
            print(scoring_string(score_method, points_this_round))
            score_count += points_this_round
            for i in range(len(SCORING_METHODS)):
                if score_method in SCORING_METHODS[i]:
                    score_card[i] = points_this_round
        else:
            print()
        mark_method_used(score_method, score_method_unused)
        display_scorecard(score_card)

        round_count += 1

    print(f'Your final score was {score_count}')


if __name__ == '__main__':
    # Asks user how many rounds to play
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)
