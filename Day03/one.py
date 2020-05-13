# Author: Ryan Lampe
# 5/12/2020
# Advent of Code 2016
# Day 3, Problem 1


def is_triangle(str):
    # Code left for reference
    # sides = str.split(r"\s+") # The r indicates a raw string, and special chars lose special meaning
    sides = str.split()
    for index, side in enumerate(sides):
        sides[index] = int(side)

   # for side in sides:   #This for loop doesn't work, if it's used instead of the upper for loop, it seems that the
   #     side = int(side)  #underlying objects aren't converted in the list, so the below if statement compares strings...

    if sides[0] + sides[1] <= sides[2] or sides[0] + sides[2] <= sides[1] or sides[1] + sides[2] <= sides[0]:
        return False
    return True


# Starting point
with open('input.txt', 'r') as file:
    triangles = file.readlines()

numT = 0
for triangle in triangles:
    if is_triangle(triangle):
        numT += 1

print("The number of valid triangles is %d" % numT)

#Output: 983 (Correct)