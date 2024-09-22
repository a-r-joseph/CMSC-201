"""
File:    leap_year.py
Author:  Abby Joseph
Date:    2/22/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes a user inputted year to determine whether that year was or
             will be a leap year.
"""


def main():

    year_in = int(input('Please enter a year: '))
    if year_in % 4 == 0:
        if year_in % 100 == 0:
            if year_in % 400 == 0:
                print(f'{year_in} is a leap year. ')
            else:
                print(f'{year_in} is not a leap year. ')
        else:
            print(f'{year_in} is a leap year. ')
    else:
        print(f'{year_in} is not a leap year. ')


if __name__ == '__main__':
    main()
