# Author: Ryan Lampe
# 5/18/2020
# Advent of Code 2016
# Day 5, Problem 1

import hashlib

realPasswordLength = 8
currentLength = 0
currentPassword = {}
for i in range(0, realPasswordLength): # Won't include 8
    currentPassword[i] = -1

print("Patience, this program takes several seconds to run!")

with open('input.txt') as file:
    doorId = file.readline()  # No newline, because file doesn't have newline to second line

while realPasswordLength > currentLength:
    testWord = doorId + str(i)
    testHash = hashlib.md5(testWord.encode()).hexdigest()
    i += 1
    good = True
    for c in testHash[0:5]:
        if c != "0":
            good = False
            break
    if good:
        position = int(testHash[5], 16)
        value = testHash[6]
        if 0 <= position < realPasswordLength:
            if currentPassword[position] == -1:
                currentPassword[position] = value
                currentLength += 1
                print("Found value for index: %d" % position)

print(currentPassword)



