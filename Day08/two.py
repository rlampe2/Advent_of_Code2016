# Author: Ryan Lampe
# 5/28/2020
# Advent of Code 2016
# Day 8, Problem 2

# The solution from part one was sufficient to get this answer, but I have redone
# the print function to make it more readable

import numpy

# Make print output wider
numpy.set_printoptions(suppress=True,linewidth=numpy.nan)
class Screen:
    """Create the screen display """

    # The screen is 50 x 6 (w x h) pixels
    # Initial state is every pixel off. (0)

    # Global to class
    width = 50
    height = 6

    # Constructor
    def __init__(self):
        #self.screen = numpy.zeros(Screen.height, Screen.width)
        self.screen = numpy.zeros((6, 50))

    # Rectangle from top left (0,0) to A wide and B tall
    def rect(self, a, b):
        for i in range(a):
            for j in range (b):
                self.screen[j][i] = 1

    # Pretty Print!
    def print_screen(self):
        print()
        for i in range (0, Screen.height):
            for j in range (0, Screen.width):
                if self.screen[i][j] == 1:
                    print('x ', end='')
                else:
                    print('_ ', end='')

            print()


    # Shift horizontal to the right
    def shift_row(self, row_num, amount):
        for j in range(amount):
            start_pixel = self.screen[row_num][Screen.width -1]
            for i in range(Screen.width - 2, -1, -1): # Start at second to last, copy into last, be inclusive of 0
                self.screen[row_num][i + 1] = self.screen[row_num][i]
            self.screen[row_num][0] = start_pixel

    # Shift vertical, down
    def shift_col(self, col_num, amount):
        for j in range(amount):
            start_pixel = self.screen[Screen.height - 1][col_num]
            for i in range(Screen.height - 2, -1, -1):
                self.screen[i + 1][col_num] = self.screen[i][col_num]
            self.screen[0][col_num] = start_pixel

    #Return number of active pixels
    def get_active_pixels(self):
        num_active = 0
        for i in range(Screen.width):
            for j in range(Screen.height):
                if self.screen[j][i] == 1:
                    num_active += 1
        return num_active


def execute(instruction, screen):
    if 'rect' in instruction:
        dim = instruction.split(' ')[1]
        a = int(dim.split('x')[0])
        b = int(dim.split('x')[1])
        screen.rect(a,b)
    elif 'row' in instruction:
        dim = instruction.split('=')[1]
        row = int(dim.split(' by ')[0])
        amount = int(dim.split(' by ')[1])
        screen.shift_row(row, amount)
    elif 'column' in instruction:
        dim = instruction.split('=')[1]
        col = int(dim.split(' by ')[0])
        amount = int(dim.split(' by ')[1])
        screen.shift_col(col, amount)
    else:
        print("ERROR! Unknown instruction")
        print(instruction)


display = Screen()

with open('input.txt', 'r') as file:
    instructions = file.read().splitlines()
    for instruction in instructions:
        execute(instruction, display)
    display.print_screen()
