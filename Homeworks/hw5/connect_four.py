"""
File:    connect_four.py
Author:  Abby Joseph
Date:    3/14/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes a user inputted grid and determines if that grid has connected four
             of the user's symbols.
"""
FOUR_IN_ROW = 4
FIRST_ROW = 0


def connect_four(the_grid, player_symbol):
    """
       A function to check for connect-four victories in the grid
       :param the_grid: the grid inputted by the user
       :param player_symbol: the symbol used to indicate the players pieces
       :return: True or False for whether there was a victory or not
    """

    victory_count = 0
    # check vertical
    for columns in range(len(the_grid[FIRST_ROW])):
        for rows in range(len(the_grid)):
            if the_grid[rows][columns] == player_symbol:
                victory_count += 1
                if victory_count >= FOUR_IN_ROW:
                    return True
            else:
                victory_count = 0
    # check horizontal
    for rows in range(len(the_grid)):
        for columns in range(len(the_grid[FIRST_ROW])):
            if the_grid[rows][columns] == player_symbol:
                victory_count += 1
                if victory_count >= FOUR_IN_ROW:
                    return True
            else:
                victory_count = 0

    return False


if __name__ == '__main__':

    num_of_rows = int(input('How many rows will be entered? '))
    board = []
    for row in range(num_of_rows):
        new_row = input()
        temp_list = []
        for symbol in new_row:
            temp_list.append(symbol)
        board.append(temp_list)

    print(connect_four(board, 'x'))
