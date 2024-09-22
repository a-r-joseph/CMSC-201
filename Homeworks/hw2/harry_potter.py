"""
File:    harry_potter.py
Author:  Abby Joseph
Date:    2/22/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input answers to yes and no questions to determine which
             character they are from the Harry Potter franchise.

"""


def main():

    student_hogwarts_in = input('Are you a student at Hogwarts? ')
    if student_hogwarts_in.lower() == 'yes':
        scar_in = input('Do you have a scar? ')
        if scar_in.lower() == 'yes':
            print('You\'re a wizard, Harry!')
        else:
            red_hair_in = input('Do you have red hair? ')
            if red_hair_in.lower() == 'yes':
                print('You must be a Weasley!')
            else:
                print('It\'s leviosa, not leviosa! You must be Hermoine Granger.')
    else:
        teacher_hogwarts_in = input('Are you a teacher at Hogwarts? ')
        if teacher_hogwarts_in.lower() == 'yes':
            beard_in = input('Do you have a beard? ')
            if beard_in.lower() == 'yes':
                giant_in = input('Are you part giant? ')
                if giant_in.lower() == 'yes':
                    print('You are Rubius Hagrid!')
                else:
                    print('You are Albus Dumbledore!')
            else:
                evil_in = input('Be honest... do you give off evil vibes? ')
                if evil_in.lower() == 'yes':
                    print('You must be Severus Snape.')
                else:
                    print('You are Minerva McGonagall')
        else:
            print('You are Sirius Black.')


if __name__ == '__main__':
    main()
