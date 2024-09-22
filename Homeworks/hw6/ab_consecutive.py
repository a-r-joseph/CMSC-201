"""
File:    ab_consecutive.py
Author:  Abby Joseph
Date:    4/13/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program constructs a string of a's and b's according to a user-inputted
             length and allowed amount of repeated characters.
"""


def ab_consecutive(n, allowed_cons, current_cons, current):
    """
    :param n: The length of the ab string
    :param allowed_cons: The maximum allowed number of repeated characters
    :param current_cons: The current number of repeated characters
    :param current: The current ab string
    :return: None
    """
    if n == 0:
        print(current)
    elif allowed_cons == 1:
        if not current:
            ab_consecutive(n - 1, allowed_cons, current_cons, current + 'a')
            ab_consecutive(n - 1, allowed_cons, current_cons, current + 'b')
        else:
            if current[len(current) - 1] == 'a':
                ab_consecutive(n - 1, allowed_cons, current_cons, current + 'b')
            else:
                ab_consecutive(n - 1, allowed_cons, current_cons, current + 'a')
    else:
        if not current:
            ab_consecutive(n - 1, allowed_cons, current_cons, current + 'a')
            ab_consecutive(n - 1, allowed_cons, current_cons, current + 'b')
        else:
            a_count = 1
            b_count = 1
            for i in range(len(current)):
                if i > 0:
                    if current[i] == 'a' and current[i] == current[i - 1]:
                        a_count += 1
                    else:
                        a_count = 1
                    if current[i] == 'b' and current[i] == current[i - 1]:
                        b_count += 1
                    else:
                        b_count = 1
            if a_count == allowed_cons:
                # adds a b if the maximum amount of repeated a's is reached
                new_cons = a_count
                ab_consecutive(n - 1, allowed_cons, new_cons, current + 'b')
            elif b_count == allowed_cons:
                new_cons = b_count
                ab_consecutive(n - 1, allowed_cons, new_cons, current + 'a')
            elif a_count < allowed_cons:
                new_cons = a_count
                ab_consecutive(n - 1, allowed_cons, new_cons, current + 'a')
                ab_consecutive(n - 1, allowed_cons, new_cons, current + 'b')
            elif b_count < allowed_cons:
                new_cons = b_count
                ab_consecutive(n - 1, allowed_cons, new_cons, current + 'a')
                ab_consecutive(n - 1, allowed_cons, new_cons, current + 'b')


if __name__ == '__main__':
    # Asks the user for the string length and max amount of repeated characters
    n, max_allowed = [int(x) for x in input(
        'Enter n and max allowed consecutives separated by spaces: ').split()]
    ab_consecutive(n, max_allowed, 0, '')
