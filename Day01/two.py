# Author: Ryan Lampe
# 5/11/2020
# Advent of Code 2016
# Day 1, Problem 2

from enum import IntEnum
class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    WEST = 3
    SOUTH = 2

with open('input.txt', 'r') as file:
    # No args reads whole file
    inStr = file.read()

#Treat each direction as incrementing y or x distance.
y = 0
x = 0

startingX = 0
startingY = 0

dirTokens = inStr.split(", ")

#Create a dictionary to lookup locations to see if they've been visited
visited = {"0,0": 1}
crossed = False
facing = Direction.NORTH

for movement in dirTokens:
    distance = int(movement[1:])
    # Orient
    if movement[0] == 'R':
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4

    for i in range(distance):

        if facing == Direction.NORTH:
            y += 1
            print("N")
        elif facing == Direction.EAST:
            x += 1
            print("E")
        elif facing == Direction.SOUTH:
            y -= 1
        else:
            x -= 1
            print("W")

        if not crossed:
            location = str(x) + "," + str(y)
            print(location)
            # check to see if our element is in the dictionary
            if location in visited:
                print ("HERE")
                startingX = int(location.split(",")[0])
                startingY = int(location.split(",")[1])
                crossed = True

            else:
                visited[location] = 1


print ("The coords are (%d ,%d) to (%d, %d)" % (startingX, startingY, x, y))
print ("The manahttan distance is %d" % ( (x - startingX) + (y - startingY)))
# NOT 166