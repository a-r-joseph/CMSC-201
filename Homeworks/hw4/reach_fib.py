"""
File:    reach_fib.py
Author:  Abby Joseph
Date:    3/5/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes a user inputted integer and calculates a Fibonacci number that is
             greater than or equal to that value.
"""

if __name__ == '__main__':

    base_num_in = int(input('What number should we succeed? '))
    fib_num = 1

    if base_num_in >= 1:
        fib_num_prev = 0
        n = 1
        while fib_num < base_num_in:
            fib_num_prev = fib_num - fib_num_prev
            fib_num = fib_num_prev + fib_num
            n += 1
        print(f'F{n} = {fib_num} which is greater than or equal to {base_num_in}.')
    else:
        print('Please enter a number greater than or equal to 1.')
