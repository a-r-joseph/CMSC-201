"""
File:    catalan.py
Author:  Abby Joseph
Date:    4/10/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description:
    This program uses recursion to calculate the sequence of Catalan numbers.
"""


def catalan(n):
    """
    :param n: The nth integer to calculate the nth Catalan number
    :return: The nth Catalan number
    """
    if n == 0:
        return 1
    else:
        # Calculates the Catalan number
        return (2 * (2 * n - 1) * catalan(n - 1)) // (n + 1)


if __name__ == "__main__":
    for i in range(0, 20):
        print(i, catalan(i))