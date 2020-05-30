# Author: Ryan Lampe
# 5/29/2020
# Advent of Code 2016
# Day 9, Problem 2

# My original solution is not efficient and will not work well with large inputs
# Alternative idea, keep an array representing each index, where the starting value is 1 if it corresponds to a
# character in the compressed string, or -1 if it corresponds to an instruction. Then multiply each index as we
# iterate through instructions, working right to left.

import numpy

# Testing:
#compressed = 'A(1x5)BC'
# compressed = 'A(2x2)BCD(2x2)EFG'
#compressed = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
#compressed = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

with open('input.txt', 'r') as file:
    compressed = file.read().replace('\n', '').replace('\r', '').replace(' ', '')

instructions = []
frequency = numpy.empty(len(compressed), dtype=numpy.uint64) # Type of int was overflow!
# Because I'm still holding onto the C way of things and want a C style for loop
i = 0
instr_start = 0
instr_end = 0
while instr_start < len(compressed):
    # Find which chars will be in the final string, and which are part of instructions
    while compressed[instr_start] != '(':
        frequency[instr_start] = 1
        instr_start += 1
        if instr_start == len(compressed):
            break
    instr_end = instr_start
    if instr_end == len(compressed):
        break
    while compressed[instr_end] != ')':
        frequency[instr_end] = 0
        instr_end += 1
        if instr_end == len(compressed):
            break
    # Catch the ) too!
    if instr_end < len(compressed):
        frequency[instr_end] = 0

    # pull out the instruction for later
    instructions.append(compressed[instr_start + 1: instr_end])
    # Move up our instruction start to right after end of the previous one
    instr_start = instr_end + 1

# Now that we have a list of instructions, and indexes, we go backwards through our compressed list
# and each time we hit a ) we read our instruction and multiply based on that instruction
i = len(compressed) - 1
while i > 0:
    # Get to next instruction
    while compressed[i] != ')':
        i -= 1
        if i == 0:
            break
    if i == 0:
        break
    instruction = instructions.pop()
    substr_len = int(instruction.split('x')[0])
    num_repeats = int(instruction.split('x')[1])
    for j in range (i + 1, i + substr_len + 1): #Don't start on '(' so plus 1
        frequency[j] *= num_repeats

    #Move on
    i -= 1


print("The decompressed files is %d chars long!" % numpy.sum(frequency))