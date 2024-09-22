"""
File:    two_bins.py
Author:  Abby Joseph
Date:    3/5/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input to keep track of items in bins based on the specific
             operations of adding, removing, transferring, and displaying what is in each bin.
"""

if __name__ == '__main__':

    a_bin = []
    b_bin = []

    action_input = input()

    while action_input != 'quit':
        temp_list = action_input.split()
        if 'A' in temp_list:
            if 'add' in temp_list:
                a_bin.append(temp_list[2])
            elif 'remove' in temp_list:
                if temp_list[2] not in a_bin:
                    print(f'Bin A does not contain \'{temp_list[2]}\'')
                else:
                    a_bin.remove(temp_list[2])
            elif 'display' in temp_list:
                print('Bin A contents: ' + ', '.join(a_bin))
            elif 'transfer' in temp_list:
                if not a_bin:
                    print('There is nothing in Bin A to transfer.')
                else:
                    b_bin.append(a_bin[0])
                    a_bin.remove(a_bin[0])
        elif 'B' in temp_list:
            if 'add' in temp_list:
                b_bin.append(temp_list[2])
            elif 'remove' in temp_list:
                if temp_list[2] not in b_bin:
                    print(f'Bin B does not contain \'{temp_list[2]}\'')
                else:
                    b_bin.remove(temp_list[2])
            elif 'display' in temp_list:
                print('Bin B contents: ' + ', '.join(b_bin))
            elif 'transfer' in temp_list:
                if not b_bin:
                    print('There is nothing in Bin A to transfer.')
                else:
                    a_bin.append(b_bin[0])
                    b_bin.remove(b_bin[0])
        action_input = input()
