"""
File:    draw_an_x.py
Author:  Abby Joseph
Date:    2/26/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user input of a size indicating length and width to draw an x-shape
             based on those measurements.
"""


if __name__ == '__main__':

    size_x_in = int(input('What is the size of the X that we want to draw? '))

    if size_x_in >= 3:
        x_shape = ''
        if size_x_in % 2 == 0:
            for i in range(size_x_in // 2):
                inner_spaces = size_x_in - (2 * (i + 1))
                for n in range(i):
                    x_shape += ' '
                x_shape += '*'
                for n in range(inner_spaces):
                    x_shape += ' '
                x_shape += '*\n'
            for i in range(size_x_in // 2):
                inner_spaces = i * 2
                outer_spaces = (size_x_in // 2) - 1 - i
                for n in range(outer_spaces):
                    x_shape += ' '
                x_shape += '*'
                for n in range(inner_spaces):
                    x_shape += ' '
                x_shape += '*\n'
        else:
            for i in range(size_x_in // 2):
                inner_spaces = size_x_in - (2 * (i + 1))
                if inner_spaces > 0:
                    for n in range(i):
                        x_shape += ' '
                    x_shape += '*'
                    for n in range(inner_spaces):
                        x_shape += ' '
                    x_shape += '*\n'
            for i in range(size_x_in // 2):
                x_shape += ' '
            x_shape += '*\n'
            for i in range(size_x_in // 2):
                inner_spaces = (i * 2) + 1
                outer_spaces = (size_x_in // 2) - 1 - i
                for n in range(outer_spaces):
                    x_shape += ' '
                x_shape += '*'
                for n in range(inner_spaces):
                    x_shape += ' '
                x_shape += '*\n'
        print(x_shape)
    else:
        print('This size is too small to produce an X shape...')
