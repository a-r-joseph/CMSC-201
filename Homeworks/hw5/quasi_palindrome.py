"""
File:    quasi_palindrome.py
Author:  Abby Joseph
Date:    3/15/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program determines if the user inputted string is a quasi-palindrome given the
             allowed number of errors.
"""
EXIT_STRING = 'quit'


def quasi_palindrome(word, errors):
    """
              A function to determine if a string is a quasi-palindrome given the allowed
              number of errors
              :param word: the string to check
              :param errors: the allowed number of errors to be a quasi-palindrome
              :return: True or False whether the word is a quasi-palindrome or not
    """

    reverse_word = []
    char_list = []
    for integer in range(len(word)):
        char_list.append(len(word) - 1 - integer)
    for i in char_list:
        reverse_word.append(word[i])
    reverse_word = ''.join(reverse_word)

    if reverse_word == word:
        return True
    else:
        error_count = 0
        for i in range(len(reverse_word)):
            if reverse_word[i] != word[i]:
                error_count += 1
        if error_count <= (2 * int(errors)):
            return True
        else:
            return False


if __name__ == '__main__':

    word_in = input('What word do you want to check? ')

    while word_in.lower() != EXIT_STRING:
        errors_in = input('How many errors do you want to allow? ')
        if int(errors_in) >= 0:
            if quasi_palindrome(word_in, errors_in):
                print(f'It was a {errors_in}-quasi-palindrome! ')
                word_in = input('What word do you want to check? ')
            else:
                print(f'It was not a {errors_in}-quasi-palindrome. ')
                word_in = input('What word do you want to check? ')
        else:
            print('Please enter a number greater than or equal to zero next time.')
            word_in = input('What word do you want to check? ')
