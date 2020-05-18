# Author: Ryan Lampe
# 5/18/2020
# Advent of Code 2016
# Day 6, Problem 2

from collections import Counter
# Have a list of lists for each index, and add all the characters in that column to it.
# Then for each list, print the most common character

index = {}


with open('input.txt', 'r') as file:
    lines = file.read().splitlines() # Use instead of readlines to get rid of newlines

for i in range(0, len(lines[0])):
    index[i] = []  # create a list at that index

for line in lines:
    for i in range(0, len(line)):
        index[i].append(line[i])

# Find most common char:
for i in range(0, len(lines[0])):
    c = Counter(index[i]).most_common()[-1]
    print(c[0])