"""
File:    rec_range.py
Author:  Abby Joseph
Date:    4/9/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description:
  This program uses recursion to produce a list of integers that would result from using the range
  function.
"""


def rec_range(start, stop, step):
    """
    :param start: The starting number of the range
    :param stop: The number that the range goes up to (but does not include)
    :param step: The number by which the range increments from start to stop
    :return: A list of integers that would be produced by the range function
    """
    if (start >= stop and step > 0) or (start <= stop and step < 0):
        return []
    elif step > 0:
        # Creates the list of integers when incrementing positively
        return [start] + rec_range(start + step, stop, step)
    elif step < 0:
        return [start] + rec_range(start - step, stop, step)


if __name__ == '__main__':
    string_list = input('Enter the range start, stop, step separated by spaces: ').split()
    int_list = []
    for s in string_list:
        int_list.append(int(s))

    start, stop, step = int_list
    print(rec_range(start, stop, step))
