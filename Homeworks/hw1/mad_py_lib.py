"""
File:    mad_py_lib.py
Author:  Abby Joseph
Date:    2/12/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input to fill in words for a mad lib.
"""


def main():

    name_in = input('Tell me your name: ')
    noun_in = input('Tell me a subject/thing (noun): ')
    adjective_in = input('Tell me an adjective: ')
    verb_in = input('Tell me a verb: ')
    second_noun_in = input('Tell me another noun: ')
    print(f'Hello {name_in}, we are going to have an amazing semester learning {noun_in}, it\'s going to be \n'
          f'{adjective_in} so don\'t worry if you need to {verb_in} from a {second_noun_in}.')


if __name__ == '__main__':
    main()
