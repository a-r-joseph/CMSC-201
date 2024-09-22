"""
File:    list_merge.py
Author:  Abby Joseph
Date:    3/1/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input of a list size and elements for two different list to
             create a merged list that alternates the elements of both.
"""


if __name__ == '__main__':

    elements_per_list = int(input('How many elements do you want in each list? '))

    if elements_per_list > 0:
        first_list = []
        second_list = []
        for element in range(elements_per_list):
            first_list.append(input('What do you want to put in the first list? '))
        for element in range(elements_per_list):
            second_list.append(input('What do you want to put in the second list? '))
        print(f'The first list is: {first_list}')
        print(f'The second list is: {second_list}')
        merged_list = []
        for i in range(elements_per_list):
            merged_list.append(first_list[i])
            merged_list.append(second_list[i])
        print(f'The merged list is: {merged_list}')
    else:
        print('Please enter a number greater than zero. ')
