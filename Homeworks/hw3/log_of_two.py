"""
File:    log_of_two.py
Author:  Abby Joseph
Date:    2/26/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input of a nth value to calculate the natural log of 2 using
             summation to the nth term.
"""


if __name__ == '__main__':

    nth_value_in = int(input('Enter the number of terms to sum: '))
    current_sum = 0

    if nth_value_in >= 1:
        for n in range(nth_value_in):
            current_sum = current_sum + (1 / ((n + 1) * (2 ** (n + 1))))
        print(f'After {nth_value_in} terms the value of ln(2) = {current_sum}')
    else:
        print('Please enter a value greater than or equal to 1.')
