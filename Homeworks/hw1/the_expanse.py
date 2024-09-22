"""
File:    the_expanse.py
Author:  Abby Joseph
Date:    2/12/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description:  This program takes user input for distance and a factor of gravity to calculate how long it will take for
              a ship in the TV show "The Expanse" to reach its target.

"""
GRAVITY = 9.8


def main():

    distance_in = float(input('What distance do you want to travel? '))
    factor_of_g_in = float(input('By what factor of g do you want to travel?'))
    seconds_time = 2 * ((distance_in / (GRAVITY * factor_of_g_in)) ** (1/2))
    hours_time = seconds_time / 3600
    days_time = seconds_time / 86400
    print(f'The amount of time a trip of {distance_in} meters will take at an acceleration of {factor_of_g_in}g is: '
          f'\n\t{seconds_time} seconds\n\t{hours_time} hours\n\t{days_time} days')


if __name__ == '__main__':
    main()
