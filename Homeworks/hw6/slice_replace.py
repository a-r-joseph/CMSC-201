"""
File:    slice_replace.py
Author:  Abby Joseph
Date:    4/13/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes an original string, finds a substring within it, and replaces it
             a new substring.
"""


def slice_replace(big_string, find_string, replace_with):
    """
    :param big_string: original user-inputted string
    :param find_string: substring to replace within the original string
    :param replace_with: substring replacement
    :return: the updated original string containing the substring replacements
    """

    if len(find_string) > 1:
        n = len(find_string)
    else:
        n = 1

    if len(big_string) == 0:
        return big_string
    else:
        if big_string[:n] == find_string:
            # replaces the substring with the substring replacement
            return replace_with + slice_replace(big_string[n:], find_string, replace_with)
        else:
            return big_string[:1] + slice_replace(big_string[1:], find_string, replace_with)


if __name__ == '__main__':
    original_string_in = input('Enter the string to use: ')
    find_string_in = input('Enter the string to find: ')
    replace_string_in = input('Enter the string to replace it with: ')
    print(slice_replace(original_string_in, find_string_in, replace_string_in))
