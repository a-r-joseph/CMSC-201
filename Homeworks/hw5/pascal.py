"""
File:    pascal.py
Author:  Abby Joseph
Date:    3/14/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program calculates the next level of Pascal's Triangle give an initial level of
             Pascal's Triangle, even if the list is not really in Pascal's Triangle.
"""
EXIT_STRING = ''


def next_level(level):
    """
          A function to determine the next level of Pascal's Triangle given an initial level
          :param level: the initial level inputted by the user
          :return: a list of the numbers that are part of the next level of Pascal's Triangle
       """

    level_list = []
    for num in level:
        level_list.append(num)

    next_level_list = []
    for index in range(len(level_list)):
        k = index - 1
        if index == 0:
            next_level_list.append(level_list[0])
        else:
            next_level_list.append(level_list[k] + level_list[index])
    next_level_list.append(level_list[(len(level_list) - 1)])

    return next_level_list


if __name__ == '__main__':
    in_string = input('What values do you want to run next_level on? ')
    while in_string != EXIT_STRING:
        values = []
        for x in in_string.split():
            values.append(int(x))
        print(next_level(values))
        in_string = input('What values do you want to run next_level on? ')
