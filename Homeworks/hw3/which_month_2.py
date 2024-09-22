"""
File:    which_month_2.py
Author:  Abby Joseph
Date:    3/1/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program determines what month it will be based on user input of a starting month
             and how many months into the future they want to go.
"""


if __name__ == '__main__':

    starting_month = int(input('What month are we starting in? (Enter as an int)'))
    list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']

    if 1 <= starting_month <= 12:
        months_into_future = int(input('How many months in the future should we go? '))
        if months_into_future > 0:
            new_month = list_of_months[((starting_month + months_into_future) % 12) - 1]
            print(f'The month will be {new_month}.')
        else:
            print('Please look into the future.')
    else:
        print('That is not a month between 1 and 12... ')
