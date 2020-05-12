# Author: Ryan Lampe
# 5/12/2020
# Advent of Code 2016
# Day 2, Problem 2



class KeyPad:
    """Create a keypad object to move around on"""

    # The above """ works like /** for javadocs
    # Conceptual Layout
    #   |   | 1 |   |
    #   | 2 | 3 | 4 |
    # 5 | 6 | 7 | 8 | 9
    #   | A | B | C |
    #   |   | D |   |

    # Class Vars (not-unique to object)

    # define special constructor
    def __init__(self):
        # Start on Number 5
        self.number = 0x5  # In hex

    def press(self):
        print("%X " % self.number)

    def move_up(self):
        if self.number in [3, 0xD]:
            self.number -= 2
        elif self.number in [6, 7, 8, 0xA, 0xB, 0xC]:
            self.number -= 4

    def move_down(self):#TODO
        if self.number in [1, 0xB]:
            self.number += 2
        elif self.number in [2, 3, 4, 6, 7, 8]:
            self.number += 4

    def move_left(self):
        if not(self.number == 1 or self.number == 2 or self.number == 5 or self.number == 0xA or self.number == 0xD):
            self.number -= 1

    def move_right(self):
        if not(self.number == 1 or self.number == 4 or self.number == 9 or self.number == 0xC or self.number == 0xD):
            self.number += 1

    def reset(self):
        self.number = 5


pad = KeyPad()

# Open the file for reading input
# Use the with syntax so that the file closes when finished
with open('input.txt', 'r') as file:
    # return array of lines
    presses = file.readlines()

print("Press these buttons")

# Array of strings representing button movements

for movement in presses:
    for direction in movement:
        if direction == "U":
            pad.move_up()
        elif direction == "R":
            pad.move_right()
        elif direction == "L":
            pad.move_left()
        elif direction == "D":
            pad.move_down()

    pad.press()