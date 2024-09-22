"""
File:    py_coin.py
Author:  Abby Joseph
Date:    2/12/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input to convert the prices of chosen items from dollars to py-coins.
"""


def main():

    in_pycoin_value_dollars = float(input("How many dollars is a py-coin now? "))
    in_item_name = input("What item do you want to convert to py-coins? ")
    in_item_price = float(input("How many dollars is the item you want to buy? "))
    price_in_pycoins = in_item_price / in_pycoin_value_dollars
    print(f"The value of a {in_item_name} in py-coins is {price_in_pycoins}.")


if __name__ == '__main__':
    main()
