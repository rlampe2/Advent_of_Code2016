# Author: Ryan Lampe
# 5/12/2020
# Advent of Code 2016
# Day 2, Problem 1


class KeyPad:
    """Create a keypad object to move around on"""

    # The above """ works like /** for javadocs
    # Conceptual Layout
    # 1 | 2 | 3
    # - - - - -
    # 4 | 5 | 6
    # - - - -  -
    # 7 | 8 | 9

    # Class Vars (not-unique to object)

    # define special constructor
    def __init__(self):
        # Start on Number 5
        self.number = 5  # This creates object field number

    def press(self):
        print("%d " % self.number)

    def move_up(self):
        if not (self.number == 1 or self.number == 2 or self.number == 3):
            self.number -= 3

    def move_down(self):
        if not(self.number == 7 or self.number == 8 or self.number == 9):
            self.number += 3

    def move_left(self):
        if not(self.number == 1 or self.number == 4 or self.number == 7):
            self.number -= 1

    def move_right(self):
        if not(self.number == 3 or self.number == 6 or self.number == 9):
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


print("\n Alternate Approach:")
# Non object approach: Treat as XY Cords for above grid
    # eg -1 1 corresponds to 9
with open('input.txt', 'r') as file:
    content = file.readlines()

ups = 0
rights = 0

for line in content:
    for char in line:
        if char == "U" and ups < 1:
            ups += 1
        elif char == "D" and ups > -1:
            ups -= 1
        elif char == "R" and rights < 1:
            rights += 1
        elif char == "L" and rights > -1:
            rights -= 1
    print("%d %d" % (ups, rights))