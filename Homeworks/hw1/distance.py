"""
File:    distance.py
Author:  Abby Joseph
Date:    2/12/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input to identify two points (x1, y1) and (x2, y2) to find the distance between
             them by using the formula for Euclidean distance.

"""


def main():

    in_float_x1 = float(input('Enter x_1: '))
    in_float_y1 = float(input('Enter y_1: '))
    in_float_x2 = float(input('Enter x_2: '))
    in_float_y2 = float(input('Enter y_2: '))
    distance = (((in_float_x2 - in_float_x1) ** 2) + ((in_float_y2 - in_float_y1) ** 2)) ** (1 / 2)
    print(f'The distance from ({in_float_x1}, {in_float_y1}) to ({in_float_x2}, {in_float_y2}) is {distance}.')


if __name__ == '__main__':
    main()
