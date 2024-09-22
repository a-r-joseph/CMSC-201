"""
File:    py_match.py
Author:  Abby Joseph
Date:    4/20/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description:
    This program allows the user to play a memory game where they have to guess and match random
    symbols.

"""
import random

COVERED = False
NOT_COVERED = True


def create_symbol_board(rows, cols, file):
    """
    A function to create the game board of random symbols
    :param rows: How many rows the game board should have
    :param cols: How many columns the game board should have
    :param file: The symbols that can be used on the game board (located in a file)
    :return: A 2D list of symbols
    """
    game_board = []
    new_row = []
    symbols = file.split()
    for i in range(rows):
        for j in range(cols):
            # Adds a random symbol to the row in the board
            new_row.append(random.choice(symbols)[0])
        game_board.append(new_row)
        new_row = []

    return game_board


def create_memory_board(rows, cols):
    """
    A function to create a parallel 2D list that indicates if the positioned symbol has been
    revealed
    :param rows: How many rows are in the game board
    :param cols: How many columns are in the game board
    :return: A boolean list that parallels the game board of symbols
    """
    mem_board = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            # Adds a bool to the row indicating that the parallel symbol has not been revealed
            new_row.append(COVERED)
        mem_board.append(new_row)

    return mem_board


def display_board(mem_board, symbol_board):
    """
    A function the display the game board used for making guesses
    :param mem_board: The 2D bool list that indicates if the parallel symbol has been revealed
    :param symbol_board: The 2D list of random symbols
    :return: None
    """
    for row in range(len(mem_board)):
        for col in range(len(mem_board)):
            if mem_board[row][col] == COVERED:
                # Prints a . for unrevealed symbols so the user can guess
                print('.', end=' ')
            else:
                print(symbol_board[row][col], end=' ')
        print()


def take_guesses(mem_board, symbol_board):
    """
    A function to take the user's guesses and allow them to try to make matches
    :param mem_board: The 2D bool list that indicates if the parallel symbol has been revealed
    :param symbol_board: The 2D list of random symbols
    :return: None
    """

    revealed_indexes = []

    # Asks the user which position on the board they want to uncover/reveal
    x_y = input('Enter position to guess: ')
    if len(x_y.split()) == 2:
        x = int((x_y.split())[0]) - 1
        y = int((x_y.split())[1]) - 1
        no_match = False

        if x in range(len(mem_board[0])) and y in range(len(mem_board)):
            while not no_match:
                if x in range(len(mem_board[0])) and y in range(len(mem_board)):
                    if mem_board[x][y] == COVERED:
                        symbol_found = symbol_board[x][y]
                        symbol_counter = 0
                        for row in range(len(mem_board)):
                            for col in range(len(mem_board[row])):
                                if symbol_board[row][col] == symbol_found:
                                    symbol_counter += 1
                        mem_board[x][y] = NOT_COVERED
                        if symbol_counter - 1 == 0:
                            print(f'You have found all of the {symbol_found}!')
                            no_match = True
                        else:
                            revealed_indexes.append([x, y])
                            while symbol_counter - 1 > 0 and not no_match:
                                display_board(mem_board, symbol_board)
                                x_y = input(f'Enter position to guess that matches {symbol_found}, '
                                             f'there are {symbol_counter - 1} remaining: ')
                                if len(x_y.split()) == 2:
                                    x = int((x_y.split())[0]) - 1
                                    y = int((x_y.split())[1]) - 1
                                    if x in range(len(mem_board[0])) and y in range(len(mem_board)):
                                        if mem_board[x][y] == COVERED:
                                            new_symbol = symbol_board[x][y]
                                            if new_symbol == symbol_found:
                                                symbol_counter -= 1
                                                mem_board[x][y] = NOT_COVERED
                                                revealed_indexes.append([x, y])
                                            else:
                                                print('No match this time:')
                                                display_board(mem_board, symbol_board)
                                                for coords in revealed_indexes:
                                                    mem_board[coords[0]][coords[1]] = COVERED
                                                no_match = True
                                                print('Try again!')
                                        else:
                                            print('That position has already been revealed. Please enter a new '
                                                  'one.')
                                    else:
                                        if not (1 <= x + 1 <= len(mem_board[0])):
                                            print(
                                                f'The position {x + 1} must be between 1 and {len(mem_board[0])}'
                                                f'.')
                                        if not (1 <= y + 1 <= len(mem_board)):
                                            print(
                                                f'The position {y + 1} must be between 1 and {len(mem_board)}.')
                                else:
                                    print('Please enter two integers seperated by a space.')
                            if symbol_counter - 1 == 0:
                                print(f'You have found all of the {symbol_found}!')
                                no_match = True
                    else:
                        x_y = input('That position has already been revealed. Please enter a new one'
                                     ': ')
                        while len(x_y.split()) != 2:
                            print('Please enter two integers seperated by a space.')
                            x_y = input('Enter a position to guess: ')
                        x = int((x_y.split())[0]) - 1
                        y = int((x_y.split())[1]) - 1

                else:
                    if not (1 <= x + 1 <= len(mem_board[0])):
                        print(f'The position {x + 1} must be between 1 and {len(mem_board[0])}'
                              f'.')
                    if not (1 <= y + 1 <= len(mem_board)):
                        print(f'The position {y + 1} must be between 1 and {len(mem_board)}.')
                    while not (1 <= x + 1 <= len(mem_board[0])) or not (1 <= y + 1 <= len(mem_board)):
                        if not (1 <= x + 1 <= len(mem_board[0])):
                            print(f'The position {x + 1} must be between 1 and {len(mem_board[0])}'
                                  f'.')
                        if not (1 <= y + 1 <= len(mem_board)):
                            print(f'The position {y + 1} must be between 1 and {len(mem_board)}.')
                        x_y = input('Enter a position to guess: ')
                        while len(x_y.split()) != 2:
                            print('Please enter two integers seperated by a space.')
                            x_y = input('Enter a position to guess: ')
                        x = int((x_y.split())[0]) - 1
                        y = int((x_y.split())[1]) - 1
        else:
            if not (1 <= x + 1 <= len(mem_board[0])):
                print(f'The position {x + 1} must be between 1 and {len(mem_board[0])}'
                      f'.')
            if not (1 <= y + 1 <= len(mem_board)):
                print(f'The position {y + 1} must be between 1 and {len(mem_board)}.')
    else:
        print('Please enter two integers seperated by a space.')


def check_victory(mem_board):
    """
    A function to check if the game has been completed and all symbols have been matched
    :param mem_board: The 2D bool list that indicates if the parallel symbol has been revealed
    :return: True or False depending on if all the symbols have been correctly matched
    """
    for row in range(len(mem_board)):
        for col in range(len(mem_board)):
            if mem_board[row][col] == COVERED:
                # There is no victory if any of the symbols are still covered after a guess
                return False
    return True


def play_py_match():
    """
    A function to allow the user to play the game
    :return: None
    """
    # Asks the user the parameters for the size of the game board
    row, col, seed = input('Please enter the rows, columns, and seed: ').split(',')
    row = int(row)
    col = int(col)
    seed = int(seed)
    random.seed(seed)
    symbol_file_in = (open(input('What is the symbol file name? '))).read()

    victory = False
    sym_board = create_symbol_board(row, col, symbol_file_in)
    memory_board = create_memory_board(row, col)

    while not victory:
        display_board(memory_board, sym_board)
        take_guesses(memory_board, sym_board)

        victory = check_victory(memory_board)

    display_board(memory_board, sym_board)
    print('Congratulations! You win!')


if __name__ == '__main__':
    play_py_match()
