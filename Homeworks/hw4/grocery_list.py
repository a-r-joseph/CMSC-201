"""
File:    grocery_list.py
Author:  Abby Joseph
Date:    3/5/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input of what was picked up at a grocery store to display what
             was bought and what groceries are still needed.
"""

if __name__ == '__main__':

    needed_items_list = ['eggs', 'bread', 'butter', 'milk']
    bought_list = []
    item_bought = input('What did you pick up in the store? ')

    while item_bought.lower() != 'quit':
        bought_list.append(item_bought)
        item_bought = input('What did you pick up in the store? ')

    for item in bought_list:
        if item in needed_items_list:
            needed_items_list.remove(item)

    if not needed_items_list:
        print('You have everything you need')
    else:
        print('You still need ' + ', '.join(needed_items_list) + '.')

    print('You bought ' + ', '.join(bought_list) + '.')
