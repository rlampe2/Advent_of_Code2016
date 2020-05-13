# Author: Ryan Lampe
# 5/13/2020
# Advent of Code 2016
# Day 3, Problem 1


def is_triangle(str):
    # Code left for reference
    # sides = str.split(r"\s+") # The r indicates a raw string, and special chars lose special meaning
    sides = str.split()
    for index, side in enumerate(sides):
        sides[index] = int(side)

    if sides[0] + sides[1] <= sides[2] or sides[0] + sides[2] <= sides[1] or sides[1] + sides[2] <= sides[0]:
        return False
    return True


# Entry point
with open('input.txt', 'r') as file:
    rawInput = file.readlines()

# Create list of side lengths
sideList = []
for row in rawInput:
    singleSide = row.split()[0]
    sideList.append(singleSide)

for row in rawInput:
    singleSide = row.split()[1]
    sideList.append(singleSide)

for row in rawInput:
    singleSide = row.split()[2]
    sideList.append(singleSide)

numT = 0   # Start, Stop, Step (doesn't include stop value)
for i in range(0, len(sideList), 3):
    triangle = sideList[i] + " " + sideList[i + 1] + " " + sideList[i + 2]
    if is_triangle(triangle):
        numT += 1

print("The number of valid triangles is %d" % numT)
