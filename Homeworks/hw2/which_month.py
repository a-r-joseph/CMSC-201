"""
File:    which_month.py
Author:  Abby Joseph
Date:    2/22/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input to determine what month it will be considering a starting
             month and how many months into the future the user wants to go.
"""


def main():

    starting_month_in = int(input('What month are we starting in? (Enter as an int)'))
    if starting_month_in > 12 or starting_month_in < 1:
        print('This is not a month between 1 and 12.')
    else:
        future_months_in = int(input('How many months into the future should we go? '))
        if future_months_in < 0:
            print('Please look towards the future.')
        else:
            new_month = (starting_month_in + future_months_in) % 12

            if new_month == 1:
                print('The month will be January.')
            elif new_month == 2:
                print('The month will be February.')
            elif new_month == 3:
                print('The month will be March.')
            elif new_month == 4:
                print('The month will be April.')
            elif new_month == 5:
                print('The month will be May.')
            elif new_month == 6:
                print('The month will be June.')
            elif new_month == 7:
                print('The month will be July.')
            elif new_month == 8:
                print('The month will be August.')
            elif new_month == 9:
                print('The month will be September.')
            elif new_month == 10:
                print('The month will be October.')
            elif new_month == 11:
                print('The month will be November.')
            elif new_month == 0:
                print('The month will be December.')


if __name__ == '__main__':
    main()
