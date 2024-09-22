"""
File:    will_it_float.py
Author:  Abby Joseph
Date:    2/22/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user inputted information about an object to determine if the
             object will float, sink, or have neutral buoyancy in water.

"""


def main():

    object_name_in = input('What is the object that we will put into the water? ')
    object_weight_in = float(input(f'What is the weight of the {object_name_in}? '))
    object_vol_in = float(input(f'What is the volume of the {object_name_in}? '))
    object_density = object_weight_in / object_vol_in

    if object_density < 1000:
        print(f'The {object_name_in} floated in the water!')
    elif object_density == 1000:
        print(f'The {object_name_in} had neutral buoyancy in the water.')
    else:
        print(f'The {object_name_in} sank in the water...')


if __name__ == '__main__':
    main()
