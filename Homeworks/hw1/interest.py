"""
File:    interest.py
Author:  Abby Joseph
Date:    2/12/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input about loan information to calculate the monthly cost of the loan.
"""


def main():

    loan_amount_in = float(input('What is the principal of the loan? '))
    interest_rate_in = float(input('What is the interest rate? '))
    length_loan_in = float(input('What is the length of the loan in years? '))
    payment_periods = length_loan_in * 12
    monthly_interest = interest_rate_in / 12
    monthly_cost = ((loan_amount_in * monthly_interest * ((1 + monthly_interest) ** payment_periods)) /
                    (((1 + monthly_interest) ** payment_periods) - 1))
    print(f'The monthly cost of the loan is {monthly_cost}.')


if __name__ == '__main__':
    main()
