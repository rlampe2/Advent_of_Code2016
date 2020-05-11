# Author: Ryan Lampe
# 5/11/2020
# Advent of Code 2016
# Day 1, Problem 1

#Treat each direction as incrementing either y or x coord, based on face

#These need to be IntEnum so that they can be added
from enum import IntEnum
class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    WEST = 2
    SOUTH = 3

# Open the file for reading input
# Use the with syntax so that the file closes when finished
with open('input.txt', 'r') as file:
    # No args reads whole file
    inStr = file.read()

#Treat each direction as incrementing y or x distance.
y = 0
x = 0
#Array of strings representing direction tokens
dirTokens = inStr.split(", ")

facing = Direction.NORTH
#should follow order of object (in order for arrays)
for movement in dirTokens:
    distance = int(movement[1:])
    #Orient
    if movement[0] == 'R':
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4

    if facing == Direction.NORTH:
        y += distance
    elif facing == Direction.EAST:
        x += distance
    elif facing == Direction.SOUTH:
        y -= distance
    else:
        x -= distance

print ("The coords are (0,0) to (%d, %d)" % (x, y))
print ("The manahttan distance is %d" % (x + y))