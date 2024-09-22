"""
File:    knobs_and_switches.py
Author:  Abby Joseph
Date:    2/22/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program utilizes user input describing the settings of knobs and a switch to play
             an RPG where they try to open a door to a treasure room.
"""


def main():

    first_knob_in = int(input('What is the position of the first knob? (Enter 1-12) '))
    second_knob_in = int(input('What is the position of the second knob? (Enter 1-12)'))
    switch_in = input('What is the position of the switch? (Enter up or down)')

    if (first_knob_in < 1 or first_knob_in > 12) and (second_knob_in < 1 or second_knob_in > 12):
        print('The knobs need to be set to 1-12.')
    elif first_knob_in < 1 or first_knob_in > 12:
        print('Knob 1  needs to be set to 1-12.')
    elif second_knob_in < 1 or second_knob_in > 12:
        print('Knob 2  needs to be set to 1-12.')
    elif switch_in.lower() != 'up' and switch_in.lower() != 'down':
        print('The switch needs to be toggled to up or down.')
    elif first_knob_in % 2 == 0:
        if second_knob_in % 2 != 0:
            if switch_in.lower() == 'up':
                print('The door opens, you get all the loot!')
            else:
                print('The door clanks but does not open, try again.')
        else:
            print('The door clanks but does not open, try again.')
    elif second_knob_in % 2 != 0:
        print('The door clanks but does not open, try again.')
    else:
        print('The handle doesn\'t budge...')


if __name__ == '__main__':
    main()
