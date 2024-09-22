"""
File:    fast_food.py
Author:  Abby Joseph
Date:    3/13/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user inputted items and calculates the total price of the order
             given predetermined prices and combos.
"""
EXIT_STRING = 'place order'


def fast_food_receipt(order):
    """
          A function to find the total price of an inputted food order
          :param order: a list of the items ordered
          :return: the int total price of the order
       """

    price = 0
    burger_counter = 0
    fries_counter = 0
    drink_counter = 0

    for item in order:
        if item in ['burger', 'sandwich']:
            price += 5
            burger_counter += 1
        elif item in ['fries']:
            price += 3
            fries_counter += 1
        elif item in ['coke', 'sprite', 'mountain dew']:
            price += 2.5
            drink_counter += 1
        else:
            price += 4

    if burger_counter <= fries_counter and burger_counter <= drink_counter:
        price -= burger_counter * 2
    elif fries_counter <= burger_counter and fries_counter <= drink_counter:
        price -= fries_counter * 2
    elif drink_counter <= burger_counter and drink_counter <= burger_counter:
        price -= drink_counter * 2

    return price


if __name__ == '__main__':
    food_order = []
    food_item = input('What would you like to order? ').lower()
    while food_item != EXIT_STRING:
        food_order.append(food_item)
        food_item = input('What would you like to order? ').lower()

    print(f'The total bill is ${fast_food_receipt(food_order)}')
